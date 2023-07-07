# # from database import db
# # from datetime import datetime

# # class Supplier(db.Model):
# #     __tablename__ = 'supplier'

# #     supplier_id = db.Column(db.Integer, primary_key=True)
# #     name = db.Column(db.String(255), nullable=False)
# #     address = db.Column(db.String)
# #     contact = db.Column(db.String)

# #     # Relationship with products
# #     products = db.relationship("Product",back_populates="suppliers")
# #     supplier_orders = db.relationship("SupplierOrder", back_populates="supplier")
# #     supplier_transactions = db.relationship("SupplierTransaction", back_populates="supplier")

# # class Product(db.Model):
# #     __tablename__ = 'product'

# #     product_id = db.Column(db.Integer, primary_key=True)
# #     name = db.Column(db.String(255), nullable=False)
# #     description = db.Column(db.String)
# #     price = db.Column(db.Numeric(10, 2), nullable=False)

# #     # Relationship with suppliers
# #     suppliers = db.relationship("Supplier",back_populates="products")
# #     supplier_orders = db.relationship("SupplierOrder", back_populates="product")
# #     stocks = db.relationship("Stock", back_populates="product")
# #     consumer_orders = db.relationship("ConsumerOrder", back_populates="product")

# # class Stock(db.Model):
# #     __tablename__ = 'stock'

# #     stock_id = db.Column(db.Integer, primary_key=True)
# #     product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'))
# #     quantity = db.Column(db.Integer, nullable=False)
# #     location = db.Column(db.String)
# #     threshold = db.Column(db.Integer, nullable=False)


# #     product = db.relationship("Product", back_populates="stocks")
# #     supplier_orders = db.relationship("SupplierOrder", back_populates="stock")
# #     consumer_transactions = db.relationship("ConsumerTransaction", back_populates="stock")

# # class SupplierOrder(db.Model):
# #     __tablename__ = 'supplier_order'

# #     order_id = db.Column(db.Integer, primary_key=True)
# #     supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.supplier_id'))
# #     product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'))
# #     stock_id = db.Column(db.Integer, db.ForeignKey('stock.stock_id'))
# #     quantity = db.Column(db.Integer, nullable=False)
# #     total_price = db.Column(db.Numeric(10, 2), nullable=False)
# #     order_date = db.Column(db.DateTime, nullable=False)

# #     supplier = db.relationship("Supplier", back_populates="supplier_orders")
# #     product = db.relationship("Product", back_populates="supplier_orders")
# #     stock = db.relationship("Stock", back_populates="supplier_orders")

# #     def calculate_total_price(self):
# #         if self.product:
# #             self.total_price = self.quantity * self.product.price

# # class SupplierTransaction(db.Model):
# #     __tablename__ = 'supplier_transaction'

# #     transaction_id = db.Column(db.Integer, primary_key=True)
# #     supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.supplier_id'))
# #     order_id = db.Column(db.Integer, db.ForeignKey('supplier_order.order_id'))
# #     amount = db.Column(db.Numeric(10, 2), nullable=False)
# #     transaction_date = db.Column(db.DateTime, nullable=False)

# #     supplier = db.relationship("Supplier", back_populates="supplier_transactions")
# #     order = db.relationship("SupplierOrder", backref="transactions")

# #     def set_amount_from_order(self):
# #         if self.order:
# #             self.amount = self.order.total_price

# # class Consumer(db.Model):
# #     __tablename__ = 'consumer'

# #     consumer_id = db.Column(db.Integer, primary_key=True)
# #     name = db.Column(db.String(255), nullable=False)
# #     address = db.Column(db.String)
# #     contact = db.Column(db.String)

# #     # Relationship with products
# #     products = db.relationship("Product", secondary='consumer_product')
# #     consumer_orders = db.relationship("ConsumerOrder",back_populates="consumer")
# #     consumer_transactions = db.relationship("ConsumerTransaction", back_populates="consumer")

# # class ConsumerOrder(db.Model):
# #     __tablename__ = 'consumer_order'

# #     order_id = db.Column(db.Integer, primary_key=True)
# #     consumer_id = db.Column(db.Integer, db.ForeignKey('consumer.consumer_id'))
# #     product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'))
# #     quantity = db.Column(db.Integer, nullable=False)
# #     total_price = db.Column(db.Numeric(10, 2), nullable=False)
# #     order_date = db.Column(db.DateTime, nullable=False)

# #     consumer = db.relationship("Consumer", back_populates="consumer_orders")
# #     product = db.relationship("Product", back_populates="consumer_orders")

# #     def calculate_total_price(self):
# #         if self.product:
# #             self.total_price = self.quantity * self.product.price

# # class ConsumerTransaction(db.Model):
# #     __tablename__ = 'consumer_transaction'

# #     transaction_id = db.Column(db.Integer, primary_key=True)
# #     consumer_id = db.Column(db.Integer, db.ForeignKey('consumer.consumer_id'))
# #     order_id = db.Column(db.Integer, db.ForeignKey('consumer_order.order_id'))
# #     stock_id = db.Column(db.Integer, db.ForeignKey('stock.stock_id'))
# #     amount = db.Column(db.Numeric(10, 2), nullable=False)
# #     transaction_date = db.Column(db.DateTime, nullable=False)

# #     consumer = db.relationship("Consumer", back_populates="consumer_transactions")
# #     order = db.relationship("ConsumerOrder", backref="transactions")
# #     stock = db.relationship("Stock", back_populates="consumer_transactions")

# #     def set_amount_from_order(self):
# #         if self.order:
# #             self.amount = self.order.total_price
# from database import db
# from datetime import datetime

# class Supplier(db.Model):
#     _tablename_ = 'supplier'

#     supplier_id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(255), nullable=False)
#     address = db.Column(db.String)
#     contact = db.Column(db.String)

#     # Relationship with products
#     # products = db.relationship("Product", back_populates="suppliers")
#     # supplier_orders = db.relationship("SupplierOrder", back_populates="supplier")
#     # supplier_transactions = db.relationship("SupplierTransaction", back_populates="supplier")

# class Product(db.Model):
#     __tablename__ = 'product'

#     product_id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(255), nullable=False)
#     description = db.Column(db.String)
#     price = db.Column(db.Numeric(10, 2), nullable=False)

#     supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.supplier_id'))
#     supplier = db.relationship("Supplier", back_populates="supplier_products")
#     supplier_orders = db.relationship("SupplierOrder", backref="product")  # Add this line

#     # Add other relationships and properties as needed


# class Stock(db.Model):
#     _tablename_ = 'stock'

#     stock_id = db.Column(db.Integer, primary_key=True)
#     product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'))
#     quantity = db.Column(db.Integer, nullable=False)
#     location = db.Column(db.String)

#     #product = db.relationship("Product", back_populates="stocks")
#     #supplier_orders = db.relationship("SupplierOrder", back_populates="stock")
#     #consumer_transactions = db.relationship("ConsumerTransaction", back_populates="stock")

# class SupplierOrder(db.Model):
#     __tablename__ = 'supplier_order'

#     order_id = db.Column(db.Integer, primary_key=True)
#     supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.supplier_id'))
#     product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'))
#     stock_id = db.Column(db.Integer, db.ForeignKey('stock.stock_id'))
#     quantity = db.Column(db.Integer, nullable=False)
#     total_price = db.Column(db.Numeric(10, 2), nullable=False)
#     order_date = db.Column(db.DateTime, nullable=False)

#     supplier = db.relationship("Supplier", backref="supplier_orders")
#     related_product = db.relationship("Product", back_populates="supplier_orders")
#     stock = db.relationship("Stock", back_populates="supplier_orders")

#     def calculate_total_price(self):
#         if self.related_product:
#             self.total_price = self.quantity * self.related_product.price


# class SupplierTransaction(db.Model):
#     _tablename_ = 'supplier_transaction'

#     id = db.Column(db.Integer, primary_key=True)
#     supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.supplier_id'))
#     order_id = db.Column(db.Integer, db.ForeignKey('supplier_order.id'))
#     amount = db.Column(db.Numeric(10, 2), nullable=False)
#     transaction_date = db.Column(db.DateTime, nullable=False)

#     #supplier = db.relationship("Supplier", back_populates="supplier_transactions")
#     order = db.relationship("SupplierOrder", backref="transactions")

#     def set_amount_from_order(self):
#         if self.order:
#             self.amount = self.order.total_price

# class Consumer(db.Model):
#     _tablename_ = 'consumer'

#     consumer_id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(255), nullable=False)
#     address = db.Column(db.String)
#     contact = db.Column(db.String)

#     # Relationship with products
#     # products = db.relationship("Product", secondary='consumer_product')
#     # consumer_orders = db.relationship("ConsumerOrder",back_populates="consumer")
#     # consumer_transactions = db.relationship("ConsumerTransaction", back_populates="consumer")

# class ConsumerOrder(db.Model):
#     _tablename_ = 'consumer_order'

#     id = db.Column(db.Integer, primary_key=True)
#     consumer_id = db.Column(db.Integer, db.ForeignKey('consumer.consumer_id'))
#     product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'))
#     quantity = db.Column(db.Integer, nullable=False)
#     total_price = db.Column(db.Numeric(10, 2), nullable=False)
#     order_date = db.Column(db.DateTime, nullable=False)

#     #consumer = db.relationship("Consumer", back_populates="consumer_orders")
#     #product = db.relationship("Product", back_populates="consumer_orders")

    # def calculate_total_price(self):
    #     if self.product:
    #         self.total_price = self.quantity * self.product.price

# class ConsumerTransaction(db.Model):
#     _tablename_ = 'consumer_transaction'

#     id = db.Column(db.Integer, primary_key=True)
#     consumer_id = db.Column(db.Integer, db.ForeignKey('consumer.consumer_id'))
#     order_id = db.Column(db.Integer, db.ForeignKey('consumer_order.id'))
#     stock_id = db.Column(db.Integer, db.ForeignKey('stock.id'))
#     amount = db.Column(db.Numeric(10, 2), nullable=False)
#     transaction_date = db.Column(db.DateTime, nullable=False)

#     #consumer = db.relationship("Consumer", back_populates="consumer_transactions")
#     order = db.relationship("ConsumerOrder", backref="transactions")
#     #stock = db.relationship("Stock", back_populates="consumer_transactions")

    # def set_amount_from_order(self):
    #     if self.order:
    #         self.amount = self.order.total_price

from database import db
from datetime import datetime

class Supplier(db.Model):
    __tablename__ = 'supplier'

    supplier_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String)
    contact = db.Column(db.String)

class Product(db.Model):
    __tablename__ = 'product'

    product_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    # supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.supplier_id', ondelete='CASCADE'), nullable=False)
    # supplier = db.relationship("Supplier", backref="products")

class Stock(db.Model):
    __tablename__ = 'stock'

    stock_id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.product_id', ondelete='CASCADE'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String)
    threshold = db.Column(db.Integer, nullable=False)
    product = db.relationship("Product", backref="stocks")

# class SupplierOrder(db.Model):
#     __tablename__ = 'supplier_order'

#     order_id = db.Column(db.Integer, primary_key=True)
#     supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.supplier_id', ondelete='CASCADE'), nullable=False)
#     product_id = db.Column(db.Integer, db.ForeignKey('product.product_id', ondelete='CASCADE'), nullable=False)
#     quantity = db.Column(db.Integer, nullable=False)
#     total_price = db.Column(db.Numeric(10, 2), nullable=False)
#     order_date = db.Column(db.DateTime, nullable=False)
#     supplier = db.relationship("Supplier", backref="supplier_orders")
#     product = db.relationship("Product", backref="supplier_orders")

class SupplierOrder(db.Model):
    __tablename__ = 'supplier_order'

    order_id = db.Column(db.Integer, primary_key=True)
    supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.supplier_id', ondelete='CASCADE'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.product_id', ondelete='CASCADE'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Numeric(10, 2), nullable=False)
    order_date = db.Column(db.DateTime, nullable=False)
    supplier = db.relationship("Supplier", backref=db.backref("supplier_orders", cascade="all, delete-orphan"))
    product = db.relationship("Product", backref=db.backref("supplier_orders", cascade="all, delete-orphan"))


# class SupplierTransaction(db.Model):
#     __tablename__ = 'supplier_transaction'

#     transaction_id = db.Column(db.Integer, primary_key=True)
#     supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.supplier_id', ondelete='CASCADE'), nullable=False)
#     order_id = db.Column(db.Integer, db.ForeignKey('supplier_order.order_id', ondelete='CASCADE'), nullable=False)
#     amount = db.Column(db.Numeric(10, 2), nullable=False)
#     transaction_date = db.Column(db.DateTime, nullable=False)
#     order=db.relationship("SupplierOrders",backref="supplier_transactions")
#     supplier = db.relationship("Supplier", backref="supplier_transactions")

class SupplierTransaction(db.Model):
    __tablename__ = 'supplier_transaction'

    transaction_id = db.Column(db.Integer, primary_key=True)
    supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.supplier_id', ondelete='CASCADE'), nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey('supplier_order.order_id', ondelete='CASCADE'), nullable=False)
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    transaction_date = db.Column(db.DateTime, nullable=False)
    supplier = db.relationship("Supplier", backref=db.backref("transactions", cascade="all, delete-orphan"))
    order = db.relationship("SupplierOrder", backref=db.backref("transactions", cascade="all, delete-orphan"))


class Consumer(db.Model):
    __tablename__ = 'consumer'

    consumer_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String)
    contact = db.Column(db.String)

class ConsumerOrder(db.Model):
    __tablename__ = 'consumer_order'

    order_id = db.Column(db.Integer, primary_key=True)
    consumer_id = db.Column(db.Integer, db.ForeignKey('consumer.consumer_id', ondelete='CASCADE'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.product_id', ondelete='CASCADE'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Numeric(10, 2), nullable=False)
    order_date = db.Column(db.DateTime, nullable=False)
    consumer = db.relationship("Consumer", backref="consumer_orders")
    product = db.relationship("Product", backref="consumer_orders")

    
    def calculate_total_price(self):
        if self.product:
            self.total_price = self.quantity * self.product.price

# class ConsumerTransaction(db.Model):
#     __tablename__ = 'consumer_transaction'

#     transaction_id = db.Column(db.Integer, primary_key=True)
#     consumer_id = db.Column(db.Integer, db.ForeignKey('consumer.consumer_id', ondelete='CASCADE'), nullable=False)
#     order_id = db.Column(db.Integer, db.ForeignKey('consumer_order.order_id', ondelete='CASCADE'), nullable=False)
#     stock_id = db.Column(db.Integer, db.ForeignKey('stock.stock_id', ondelete='CASCADE'), nullable=False)
#     amount = db.Column(db.Numeric(10, 2), nullable=False)
#     transaction_date = db.Column(db.DateTime, nullable=False)

#     order=db.relationship("ConsumerOrders",backref="consumer_transactions")
#     consumer = db.relationship("Consumer", backref="consumer_transactions")
class ConsumerTransaction(db.Model):
    __tablename__ = 'consumer_transaction'

    transaction_id = db.Column(db.Integer, primary_key=True)
    consumer_id = db.Column(db.Integer, db.ForeignKey('consumer.consumer_id', ondelete='CASCADE'), nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey('consumer_order.order_id', ondelete='CASCADE'), nullable=False)
    stock_id = db.Column(db.Integer, db.ForeignKey('stock.stock_id', ondelete='CASCADE'), nullable=False)
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    transaction_date = db.Column(db.DateTime, nullable=False)
    consumer = db.relationship("Consumer", backref=db.backref("transactions", cascade="all, delete-orphan"))
    order = db.relationship("ConsumerOrder", backref=db.backref("transactions", cascade="all, delete-orphan"))
    stock = db.relationship("Stock", backref=db.backref("transactions", cascade="all, delete-orphan"))

    def set_amount_from_order(self):
        if self.order:
            self.amount = self.order.total_price