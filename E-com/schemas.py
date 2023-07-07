import strawberry
from typing import List
from models import *
from dao import *

import strawberry
from typing import List


@strawberry.type
class Supplier:
    supplier_id: int
    name: str
    address: str
    contact: str


@strawberry.type
class Product:
    product_id: int
    name: str
    description: str
    price: float


@strawberry.type
class Stock:
    stock_id: int
    product_id: int
    quantity: int
    location: str
    threshold: int


@strawberry.type
class SupplierOrder:
    order_id: int
    supplier: Supplier
    product: Product
    stock: Stock
    quantity: int
    order_date: str


@strawberry.type
class Consumer:
    consumer_id: int
    name: str
    address: str
    contact: str


@strawberry.type
class ConsumerOrder:
    order_id: int
    consumer: Consumer
    product: Product
    quantity: int
    order_date: str


@strawberry.type
class ConsumerTransaction:
    transaction_id: int
    consumer: Consumer
    order: ConsumerOrder
    stock: Stock
    transaction_date: str
    amount: float


@strawberry.type
class SupplierTransaction:
    transaction_id: int
    supplier: Supplier
    order: SupplierOrder
    transaction_date: str
    amount: float


@strawberry.type
class Query:
    @strawberry.field
    def get_supplier_by_id(supplier_id: int) -> Supplier:
        return SupplierDAO.get_supplier_by_id(supplier_id)

    @strawberry.field
    def get_all_suppliers() -> List[Supplier]:
        return SupplierDAO.get_all_suppliers()

    @strawberry.field
    def get_product_by_id(product_id: int) -> Product:
        return ProductDAO.get_product_by_id(product_id)

    @strawberry.field
    def get_all_products() -> List[Product]:
        return ProductDAO.get_all_products()

    @strawberry.field
    def get_stock_by_id(stock_id: int) -> Stock:
        return StockDAO.get_stock_by_id(stock_id)

    @strawberry.field
    def get_all_stocks() -> List[Stock]:
        return StockDAO.get_all_stocks()

    @strawberry.field
    def get_supplier_order_by_id(order_id: int) -> SupplierOrder:
        return SupplierOrderDAO.get_supplier_order_by_id(order_id)

    @strawberry.field
    def get_all_supplier_orders() -> List[SupplierOrder]:
        return SupplierOrderDAO.get_all_supplier_orders()

    @strawberry.field
    def get_consumer_by_id(consumer_id: int) -> Consumer:
        return ConsumerDAO.get_consumer_by_id(consumer_id)

    @strawberry.field
    def get_all_consumers() -> List[Consumer]:
        return ConsumerDAO.get_all_consumers()

    @strawberry.field
    def get_consumer_order_by_id(order_id: int) -> ConsumerOrder:
        return ConsumerOrderDAO.get_consumer_order_by_id(order_id)

    @strawberry.field
    def get_all_consumer_orders() -> List[ConsumerOrder]:
        return ConsumerOrderDAO.get_all_consumer_orders()

    @strawberry.field
    def get_supplier_transaction_by_id(transaction_id: int) -> SupplierTransaction:
        return SupplierTransactionDAO.get_supplier_transaction_by_id(transaction_id)

    @strawberry.field
    def get_all_supplier_transactions() -> List[SupplierTransaction]:
        return SupplierTransactionDAO.get_all_supplier_transactions()

    @strawberry.field
    def get_consumer_transaction_by_id(transaction_id: int) -> ConsumerTransaction:
        return ConsumerTransactionDAO.get_consumer_transaction_by_id(transaction_id)

    @strawberry.field
    def get_all_consumer_transactions() -> List[ConsumerTransaction]:
        return ConsumerTransactionDAO.get_all_consumer_transactions()


@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_supplier(name: str, address: str, contact: str) -> Supplier:
        return SupplierDAO.create_supplier(name, address, contact)

    @strawberry.mutation
    def update_supplier(supplier_id: int, name: str = None, address: str = None, contact: str = None) -> Supplier:
        return SupplierDAO.update_supplier(supplier_id, name, address, contact)

    @strawberry.mutation
    def delete_supplier(supplier_id: int) -> Supplier:
        return SupplierDAO.delete_supplier(supplier_id)

    @strawberry.mutation
    def create_product(name: str, description: str, price: float) -> Product:
        return ProductDAO.create_product(name, description, price)

    @strawberry.mutation
    def update_product(product_id: int, name: str = None, description: str = None, price: float = None) -> Product:
        return ProductDAO.update_product(product_id, name, description, price)

    @strawberry.mutation
    def delete_product(product_id: int) -> Product:
        return ProductDAO.delete_product(product_id)

    @strawberry.mutation
    def create_stock(product_id: int, quantity: int, location: str, threshold: int) -> Stock:
        return StockDAO.create_stock(product_id, quantity, location, threshold)

    @strawberry.mutation
    def update_stock(stock_id: int, quantity: int = None, location: str = None, threshold: int = None) -> Stock:
        return StockDAO.update_stock(stock_id, quantity, location, threshold)

    @strawberry.mutation
    def delete_stock(stock_id: int) -> Stock:
        return StockDAO.delete_stock(stock_id)

    @strawberry.mutation
    def create_supplier_order(supplier_id: int, product_id: int, stock_id: int, quantity: int, order_date: str) -> SupplierOrder:
        return SupplierOrderDAO.create_supplier_order(supplier_id, product_id, stock_id, quantity, order_date)

    @strawberry.mutation
    def update_supplier_order(order_id: int, quantity: int = None, order_date: str = None) -> SupplierOrder:
        return SupplierOrderDAO.update_supplier_order(order_id, quantity, order_date)

    @strawberry.mutation
    def delete_supplier_order(order_id: int) -> SupplierOrder:
        return SupplierOrderDAO.delete_supplier_order(order_id)

    @strawberry.mutation
    def create_consumer(name: str, address: str, contact: str) -> Consumer:
        return ConsumerDAO.create_consumer(name, address, contact)

    @strawberry.mutation
    def update_consumer(consumer_id: int, name: str = None, address: str = None, contact: str = None) -> Consumer:
        return ConsumerDAO.update_consumer(consumer_id, name, address, contact)

    @strawberry.mutation
    def delete_consumer(consumer_id: int) -> Consumer:
        return ConsumerDAO.delete_consumer(consumer_id)

    @strawberry.mutation
    def create_consumer_order(consumer_id: int, product_id: int, quantity: int, order_date: str) -> ConsumerOrder:
        return ConsumerOrderDAO.create_consumer_order(consumer_id, product_id, quantity, order_date)

    @strawberry.mutation
    def update_consumer_order(order_id: int, quantity: int = None, order_date: str = None) -> ConsumerOrder:
        return ConsumerOrderDAO.update_consumer_order(order_id, quantity, order_date)

    @strawberry.mutation
    def delete_consumer_order(order_id: int) -> ConsumerOrder:
        return ConsumerOrderDAO.delete_consumer_order(order_id)

    @strawberry.mutation
    def create_supplier_transaction(supplier_id: int, order_id: int, transaction_date: str) -> SupplierTransaction:
        return SupplierTransactionDAO.create_supplier_transaction(supplier_id, order_id, transaction_date)

    @strawberry.mutation
    def update_supplier_transaction(transaction_id: int, amount: float = None, transaction_date: str = None) -> SupplierTransaction:
        return SupplierTransactionDAO.update_supplier_transaction(transaction_id, amount, transaction_date)

    @strawberry.mutation
    def delete_supplier_transaction(transaction_id: int) -> SupplierTransaction:
        return SupplierTransactionDAO.delete_supplier_transaction(transaction_id)

    @strawberry.mutation
    def create_consumer_transaction(consumer_id: int, order_id: int, stock_id: int, transaction_date: str) -> ConsumerTransaction:
        return ConsumerTransactionDAO.create_consumer_transaction(consumer_id, order_id, stock_id, transaction_date)

    @strawberry.mutation
    def update_consumer_transaction(transaction_id: int, amount: float = None, transaction_date: str = None) -> ConsumerTransaction:
        return ConsumerTransactionDAO.update_consumer_transaction(transaction_id, amount, transaction_date)

    @strawberry.mutation
    def delete_consumer_transaction(transaction_id: int) -> ConsumerTransaction:
        return ConsumerTransactionDAO.delete_consumer_transaction(transaction_id)


schema = strawberry.Schema(query=Query, mutation=Mutation)