from database import db
from datetime import datetime

class Supplier(db.Model):
    __tablename__ = 'supplier'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String)
    contact = db.Column(db.String)

    # Relationship with products
    products = db.relationship("Product", secondary='supplier_product')
    supplier_orders = db.relationship("SupplierOrder", back_populates="supplier")
    supplier_transactions = db.relationship("SupplierTransaction", back_populates="supplier")

class Product(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String)
    price = db.Column(db.Numeric(10, 2), nullable=False)

    # Relationship with suppliers
    suppliers = db.relationship("Supplier", secondary='supplier_product')
    supplier_orders = db.relationship("SupplierOrder", back_populates="product")
    stocks = db.relationship("Stock", back_populates="product")
    consumer_orders = db.relationship("ConsumerOrder", back_populates="product")

class Stock(db.Model):
    __tablename__ = 'stock'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    quantity = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String)

    product = db.relationship("Product", back_populates="stocks")
    supplier_orders = db.relationship("SupplierOrder", back_populates="stock")
    consumer_transactions = db.relationship("ConsumerTransaction", back_populates="stock")

class SupplierOrder(db.Model):
    __tablename__ = 'supplier_order'

    id = db.Column(db.Integer, primary_key=True)
    supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    stock_id = db.Column(db.Integer, db.ForeignKey('stock.id'))
    quantity = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Numeric(10, 2), nullable=False)
    order_date = db.Column(db.DateTime, nullable=False)

    supplier = db.relationship("Supplier", back_populates="supplier_orders")
    product = db.relationship("Product", back_populates="supplier_orders")
    stock = db.relationship("Stock", back_populates="supplier_orders")

    def calculate_total_price(self):
        if self.product:
            self.total_price = self.quantity * self.product.price

class SupplierTransaction(db.Model):
    __tablename__ = 'supplier_transaction'

    id = db.Column(db.Integer, primary_key=True)
    supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.id'))
    order_id = db.Column(db.Integer, db.ForeignKey('supplier_order.id'))
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    transaction_date = db.Column(db.DateTime, nullable=False)

    supplier = db.relationship("Supplier", back_populates="supplier_transactions")
    order = db.relationship("SupplierOrder", backref="transactions")

    def set_amount_from_order(self):
        if self.order:
            self.amount = self.order.total_price

class Consumer(db.Model):
    __tablename__ = 'consumer'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String)
    contact = db.Column(db.String)

    # Relationship with products
    products = db.relationship("Product", secondary='consumer_product')
    consumer_orders = db.relationship("ConsumerOrder",back_populates="consumer")
    consumer_transactions = db.relationship("ConsumerTransaction", back_populates="consumer")

class ConsumerOrder(db.Model):
    __tablename__ = 'consumer_order'

    id = db.Column(db.Integer, primary_key=True)
    consumer_id = db.Column(db.Integer, db.ForeignKey('consumer.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    quantity = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Numeric(10, 2), nullable=False)
    order_date = db.Column(db.DateTime, nullable=False)

    consumer = db.relationship("Consumer", back_populates="consumer_orders")
    product = db.relationship("Product", back_populates="consumer_orders")

    def calculate_total_price(self):
        if self.product:
            self.total_price = self.quantity * self.product.price

class ConsumerTransaction(db.Model):
    __tablename__ = 'consumer_transaction'

    id = db.Column(db.Integer, primary_key=True)
    consumer_id = db.Column(db.Integer, db.ForeignKey('consumer.id'))
    order_id = db.Column(db.Integer, db.ForeignKey('consumer_order.id'))
    stock_id = db.Column(db.Integer, db.ForeignKey('stock.id'))
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    transaction_date = db.Column(db.DateTime, nullable=False)

    consumer = db.relationship("Consumer", back_populates="consumer_transactions")
    order = db.relationship("ConsumerOrder", backref="transactions")
    stock = db.relationship("Stock", back_populates="consumer_transactions")

    def set_amount_from_order(self):
        if self.order:
            self.amount = self.order.total_price
