import strawberry
from dao import (
    create_supplier,
    get_supplier_by_id,
    get_all_suppliers,
    update_supplier,
    delete_supplier,
    create_product,
    get_product_by_id,
    get_all_products,
    update_product,
    delete_product,
    create_stock,
    get_stock_by_id,
    get_stock_by_product_id,
    get_all_stocks,
    update_stock,
    delete_stock,
    create_supplier_order,
    get_supplier_order_by_id,
    get_all_supplier_orders,
    update_supplier_order,
    delete_supplier_order,
    create_supplier_transaction,
    get_supplier_transaction_by_id,
    get_all_supplier_transactions,
)


@strawberry.type
class Supplier:
    name: str
    address: str
    contact: str


@strawberry.type
class Product:
    name: str
    description: str
    price: float


@strawberry.type
class Stock:
    product_id: int
    quantity: int
    location: str


@strawberry.type
class SupplierOrder:
    supplier_id: int
    product_id: int
    stock_id: int
    quantity: int
    order_date: str


@strawberry.type
class SupplierTransaction:
    supplier_id: int
    order_id: int
    transaction_date: str


@strawberry.type
class Query:
    @strawberry.field
    def get_supplier(self, info, supplier_id: int) -> Supplier:
        return get_supplier_by_id(info, supplier_id)

    @strawberry.field
    def get_all_suppliers(self, info) -> [Supplier]:
        return get_all_suppliers(info)

    @strawberry.field
    def get_product(self, info, product_id: int) -> Product:
        return get_product_by_id(info, product_id)

    @strawberry.field
    def get_all_products(self, info) -> [Product]:
        return get_all_products(info)

    # Add other query resolvers


@strawberry.type
class Mutation:
    create_supplier: Supplier = strawberry.mutation(resolver=create_supplier)
    update_supplier: Supplier = strawberry.mutation(resolver=update_supplier)
    delete_supplier: Supplier = strawberry.mutation(resolver=delete_supplier)
    create_product: Product = strawberry.mutation(resolver=create_product)
    update_product: Product = strawberry.mutation(resolver=update_product)
    delete_product: Product = strawberry.mutation(resolver=delete_product)
    create_stock: Stock = strawberry.mutation(resolver=create_stock)
    update_stock: Stock = strawberry.mutation(resolver=update_stock)
    delete_stock: Stock = strawberry.mutation(resolver=delete_stock)
    create_supplier_order: SupplierOrder = strawberry.mutation(resolver=create_supplier_order)
    update_supplier_order: SupplierOrder = strawberry.mutation(resolver=update_supplier_order)
    delete_supplier_order: SupplierOrder = strawberry.mutation(resolver=delete_supplier_order)
    create_supplier_transaction: SupplierTransaction = strawberry.mutation(resolver=create_supplier_transaction)
    update_supplier_transaction: SupplierTransaction = strawberry.mutation(resolver=update_supplier_transaction)
    delete_supplier_transaction: SupplierTransaction = strawberry.mutation(resolver=delete_supplier_transaction)

    # Add other mutation resolvers


schema = strawberry.Schema(query=Query, mutation=Mutation)
