

import strawberry
from typing import List
from dao import *


@strawberry.type
class Supplier:
    id: int
    name: str
    address: str
    contact: str
    products: List['Product']
    supplier_orders: List['SupplierOrder']
    supplier_transactions: List['SupplierTransaction']

    @strawberry.field
    def products(self, info) -> List['Product']:
        return ProductDAO.get_products_by_supplier_id(self.id)

    @strawberry.field
    def supplier_orders(self, info) -> List['SupplierOrder']:
        return SupplierOrderDAO.get_supplier_orders_by_supplier_id(self.id)

    @strawberry.field
    def supplier_transactions(self, info) -> List['SupplierTransaction']:
        return SupplierTransactionDAO.get_supplier_transactions_by_supplier_id(self.id)

    @strawberry.field
    def transaction_count(self, info) -> int:
        return len(self.supplier_transactions)

    @strawberry.field
    def supplier_order_count(self, info) -> int:
        return len(self.supplier_orders)

    @strawberry.field
    def product_count(self, info) -> int:
        return len(self.products)
    

@strawberry.type
class Product:
    id: int
    name: str
    description: str
    price: float
    suppliers: List[Supplier]
    supplier_orders: List['SupplierOrder']
    stocks: List['Stock']
    consumer_orders: List['ConsumerOrder']

    def resolve_suppliers(self, info) -> List[Supplier]:
        return SupplierDAO.get_suppliers_by_product_id(self.id)

    def resolve_supplier_orders(self, info) -> List['SupplierOrder']:
        return SupplierOrderDAO.get_supplier_orders_by_product_id(self.id)

    def resolve_stocks(self, info) -> List['Stock']:
        return StockDAO.get_stocks_by_product_id(self.id)

    def resolve_consumer_orders(self, info) -> List['ConsumerOrder']:
        return ConsumerOrderDAO.get_consumer_orders_by_product_id(self.id)

    @strawberry.field
    def supplier_order_count(self, info) -> int:
        return len(self.supplier_orders)

    @strawberry.field
    def stock_count(self, info) -> int:
        return len(self.stocks)

    @strawberry.field
    def consumer_order_count(self, info) -> int:
        return len(self.consumer_orders)
    

@strawberry.type
class Stock:
    id: int
    product_id: int
    quantity: int
    location: str
    product: Product
    supplier_orders: List['SupplierOrder']
    consumer_transactions: List['ConsumerTransaction']

    def resolve_product(self, info) -> Product:
        return ProductDAO.get_product_by_id(self.product_id)

    def resolve_supplier_orders(self, info) -> List['SupplierOrder']:
        return SupplierOrderDAO.get_supplier_orders_by_stock_id(self.id)

    def resolve_consumer_transactions(self, info) -> List['ConsumerTransaction']:
        return ConsumerTransactionDAO.get_consumer_transactions_by_stock_id(self.id)

    @strawberry.field
    def supplier_order_count(self, info) -> int:
        return len(self.supplier_orders)

    @strawberry.field
    def consumer_transaction_count(self, info) -> int:
        return len(self.consumer_transactions)
    
 
@strawberry.type
class SupplierOrder:
    id: int
    supplier_id: int
    product_id: int
    stock_id: int
    quantity: int
    total_price: float
    order_date: str
    supplier: Supplier
    product: Product
    stock: List[Stock]

    def resolve_supplier(self, info) -> Supplier:
        return SupplierDAO.get_supplier_by_id(self.supplier_id)

    def resolve_product(self, info) -> Product:
        return ProductDAO.get_product_by_id(self.product_id)

    def resolve_stock(self, info) -> List[Stock]:
        return StockDAO.get_stock_by_id(self.stock_id)

    @strawberry.field
    def stock_length(self, info) -> int:
        return len(self.stock)

@strawberry.type
class SupplierTransaction:
    id: int
    supplier_id: int
    order_id: int
    amount: float
    transaction_date: str
    supplier: Supplier
    order: SupplierOrder

    def resolve_supplier(self, info) -> Supplier:
        return SupplierDAO.get_supplier_by_id(self.supplier_id)

    def resolve_order(self, info) -> SupplierOrder:
        return SupplierOrderDAO.get_supplier_order_by_id(self.order_id)

    @classmethod
    def transaction_count(cls, info) -> int:
        return SupplierTransactionDAO.get_supplier_transaction_count()
@strawberry.type
class Consumer:
    id: int
    name: str
    address: str
    contact: str
    products: List[Product]
    consumer_orders: List['ConsumerOrder']
    consumer_transactions: List['ConsumerTransaction']

    def resolve_products(self, info) -> List[Product]:
        return ProductDAO.get_products_by_consumer_id(self.id)

    def resolve_consumer_orders(self, info) -> List['ConsumerOrder']:
        return ConsumerOrderDAO.get_consumer_orders_by_consumer_id(self.id)

    def resolve_consumer_transactions(self, info) -> List['ConsumerTransaction']:
        return ConsumerTransactionDAO.get_consumer_transactions_by_consumer_id(self.id)

    @strawberry.field
    def consumer_order_count(self, info) -> int:
        return len(self.consumer_orders)

    @strawberry.field
    def product_count(self, info) -> int:
        return len(self.products)

    @strawberry.field
    def consumer_transaction_count(self, info) -> int:
        return len(self.consumer_transactions)

@strawberry.type
class Consumer:
    id: int
    name: str
    address: str
    contact: str
    products: List[Product]
    consumer_orders: List['ConsumerOrder']
    consumer_transactions: List['ConsumerTransaction']

    def resolve_products(self, info) -> List[Product]:
        return ProductDAO.get_products_by_consumer_id(self.id)

    def resolve_consumer_orders(self, info) -> List['ConsumerOrder']:
        return ConsumerOrderDAO.get_consumer_orders_by_consumer_id(self.id)

    def resolve_consumer_transactions(self, info) -> List['ConsumerTransaction']:
        return ConsumerTransactionDAO.get_consumer_transactions_by_consumer_id(self.id)

    @strawberry.field
    def consumer_order_count(self, info) -> int:
        return len(self.consumer_orders)

    @strawberry.field
    def product_count(self, info) -> int:
        return len(self.products)
@strawberry.type
class ConsumerTransaction:
    id: int
    consumer_id: int
    order_id: int
    stock_id: int
    amount: float
    transaction_date: str
    consumer: Consumer
    order: ConsumerOrder
    stock: Stock

    def resolve_consumer(self, info) -> Consumer:
        return ConsumerDAO.get_consumer_by_id(self.consumer_id)

    def resolve_order(self, info) -> ConsumerOrder:
        return ConsumerOrderDAO.get_consumer_order_by_id(self.order_id)

    def resolve_stock(self, info) -> Stock:
        return StockDAO.get_stock_by_id(self.stock_id)

    @strawberry.field
    def consumer_transaction_count(self, info) -> int:
        return len(self.consumer.consumer_transactions)

    @strawberry.field
    def order_count(self, info) -> int:
        return len(self.order.consumer.consumer_orders)

@strawberry.type
class Query:
    @strawberry.field
    def all_suppliers(self) -> List[Supplier]:
        return SupplierDAO.get_all_suppliers()

    @strawberry.field
    def all_products(self) -> List[Product]:
        return ProductDAO.get_all_products()

    @strawberry.field
    def all_stocks(self) -> List[Stock]:
        return StockDAO.get_all_stocks()

    @strawberry.field
    def all_supplier_orders(self) -> List[SupplierOrder]:
        return SupplierOrderDAO.get_all_supplier_orders()

    @strawberry.field
    def all_supplier_transactions(self) -> List[SupplierTransaction]:
        return SupplierTransactionDAO.get_all_supplier_transactions()

    @strawberry.field
    def all_consumers(self) -> List[Consumer]:
        return ConsumerDAO.get_all_consumers()

    @strawberry.field
    def all_consumer_orders(self) -> List[ConsumerOrder]:
        return ConsumerOrderDAO.get_all_consumer_orders()

    @strawberry.field
    def all_consumer_transactions(self) -> List[ConsumerTransaction]:
        return ConsumerTransactionDAO.get_all_consumer_transactions()
    
    @strawberry.field
    def supplier(self, supplier_id: int) -> Supplier:
        return SupplierDAO.get_supplier_by_id(supplier_id)

    @strawberry.field
    def product(self, product_id: int) -> Product:
        return ProductDAO.get_product_by_id(product_id)

    @strawberry.field
    def stock(self, stock_id: int) -> Stock:
        return StockDAO.get_stock_by_id(stock_id)

    @strawberry.field
    def supplier_order(self, order_id: int) -> SupplierOrder:
        return SupplierOrderDAO.get_supplier_order_by_id(order_id)

    @strawberry.field
    def supplier_transaction(self, transaction_id: int) -> SupplierTransaction:
        return SupplierTransactionDAO.get_supplier_transaction_by_id(transaction_id)

    @strawberry.field
    def consumer(self, consumer_id: int) -> Consumer:
        return ConsumerDAO.get_consumer_by_id(consumer_id)

    @strawberry.field
    def consumer_order(self, order_id: int) -> ConsumerOrder:
        return ConsumerOrderDAO.get_consumer_order_by_id(order_id)

    @strawberry.field
    def consumer_transaction(self, transaction_id: int) -> ConsumerTransaction:
        return ConsumerTransactionDAO.get_consumer_transaction_by_id(transaction_id)



@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_supplier(self, name: str, address: str, contact: str) -> Supplier:
        supplier = SupplierDAO.create_supplier(name, address, contact)
        return Supplier(**supplier.__dict__)

    @strawberry.mutation
    def update_supplier(self, id: int, name: str, address: str, contact: str) -> Supplier:
        supplier = SupplierDAO.update_supplier(id, name, address, contact)
        return Supplier(**supplier.__dict__)

    @strawberry.mutation
    def delete_supplier(self, id: int) -> bool:
        return SupplierDAO.delete_supplier(id)

    @strawberry.mutation
    def create_product(self, name: str, description: str, price: float) -> Product:
        product = ProductDAO.create_product(name, description, price)
        return Product(**product.__dict__)

    @strawberry.mutation
    def update_product(self, id: int, name: str, description: str, price: float) -> Product:
        product = ProductDAO.update_product(id, name, description, price)
        return Product(**product.__dict__)

    @strawberry.mutation
    def delete_product(self, id: int) -> bool:
        return ProductDAO.delete_product(id)

    @strawberry.mutation
    def create_stock(self, product_id: int, quantity: int, location: str) -> Stock:
        stock = StockDAO.create_stock(product_id, quantity, location)
        return Stock(**stock.__dict__)

    @strawberry.mutation
    def update_stock(self, id: int, product_id: int, quantity: int, location: str) -> Stock:
        stock = StockDAO.update_stock(id, product_id, quantity, location)
        return Stock(**stock.__dict__)

    @strawberry.mutation
    def delete_stock(self, id: int) -> bool:
        return StockDAO.delete_stock(id)

    @strawberry.mutation
    def create_supplier_order(
        self,
        supplier_id: int,
        product_id: int,
        stock_id: int,
        quantity: int,
        order_date: str
    ) -> SupplierOrder:
        supplier_order = SupplierOrderDAO.create_supplier_order(
            supplier_id, product_id, stock_id, quantity, order_date
        )
        return SupplierOrder(**supplier_order.__dict__)

    @strawberry.mutation
    def update_supplier_order(
        self,
        id: int,
        supplier_id: int,
        product_id: int,
        stock_id: int,
        quantity: int,
        order_date: str
    ) -> SupplierOrder:
        supplier_order = SupplierOrderDAO.update_supplier_order(
            id, supplier_id, product_id, stock_id, quantity, order_date
        )
        return SupplierOrder(**supplier_order.__dict__)

    @strawberry.mutation
    def delete_supplier_order(self, id: int) -> bool:
        return SupplierOrderDAO.delete_supplier_order(id)

    @strawberry.mutation
    def create_supplier_transaction(
        self, supplier_id: int, order_id: int, transaction_date: str
    ) -> SupplierTransaction:
        supplier_transaction = SupplierTransactionDAO.create_supplier_transaction(
            supplier_id, order_id, transaction_date
        )
        return SupplierTransaction(**supplier_transaction.__dict__)

    @strawberry.mutation
    def update_supplier_transaction(
        self, id: int, supplier_id: int, order_id: int, transaction_date: str
    ) -> SupplierTransaction:
        supplier_transaction = SupplierTransactionDAO.update_supplier_transaction(
            id, supplier_id, order_id, transaction_date
        )
        return SupplierTransaction(**supplier_transaction.__dict__)

    @strawberry.mutation
    def delete_supplier_transaction(self, id: int) -> bool:
        return SupplierTransactionDAO.delete_supplier_transaction(id)

    @strawberry.mutation
    def create_consumer(self, name: str, address: str, contact: str) -> Consumer:
        consumer = ConsumerDAO.create_consumer(name, address, contact)
        return Consumer(**consumer.__dict__)

    @strawberry.mutation
    def update_consumer(self, id: int, name: str, address: str, contact: str) -> Consumer:
        consumer = ConsumerDAO.update_consumer(id, name, address, contact, contact)
        return Consumer(**consumer.__dict__)

    @strawberry.mutation
    def delete_consumer(self, id: int) -> bool:
        return ConsumerDAO.delete_consumer(id)

    @strawberry.mutation
    def create_consumer_order(
        self, consumer_id: int, product_id: int, quantity: int, order_date: str
    ) -> ConsumerOrder:
        consumer_order = ConsumerOrderDAO.create_consumer_order(
            consumer_id, product_id, quantity, order_date
        )
        return ConsumerOrder(**consumer_order.__dict__)

    @strawberry.mutation
    def update_consumer_order(
        self, id: int, consumer_id: int, product_id: int, quantity: int, order_date: str
    ) -> ConsumerOrder:
        consumer_order = ConsumerOrderDAO.update_consumer_order(
            id, consumer_id, product_id, quantity, order_date
        )
        return ConsumerOrder(**consumer_order.__dict__)

    @strawberry.mutation
    def delete_consumer_order(self, id: int) -> bool:
        return ConsumerOrderDAO.delete_consumer_order(id)

    @strawberry.mutation
    def create_consumer_transaction(
        self, consumer_id: int, order_id: int, stock_id: int, transaction_date: str
    ) -> ConsumerTransaction:
        consumer_transaction = ConsumerTransactionDAO.create_consumer_transaction(
            consumer_id, order_id, stock_id, transaction_date
        )
        return ConsumerTransaction(**consumer_transaction.__dict__)

    @strawberry.mutation
    def update_consumer_transaction(
        self, id: int, consumer_id: int, order_id: int, stock_id: int, transaction_date: str
    ) -> ConsumerTransaction:
        consumer_transaction = ConsumerTransactionDAO.update_consumer_transaction(
            id, consumer_id, order_id, stock_id, transaction_date
        )
        return ConsumerTransaction(**consumer_transaction.__dict__)

    @strawberry.mutation
    def delete_consumer_transaction(self, id: int) -> bool:
        return ConsumerTransactionDAO.delete_consumer_transaction(id)


schema = strawberry.Schema(query=Query, mutation=Mutation)
