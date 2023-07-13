from database import db
from datetime import datetime



class Supplier(db.Model):
    __tablename__ = 'supplier'

    supplier_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String, nullable=False)
    contact = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)

    products = db.relationship('Product', secondary='product_supplier', backref='suppliers')

class Product(db.Model):
    __tablename__ = 'product'

    product_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String)
    price = db.Column(db.Numeric(10, 2), nullable=False)

product_supplier = db.Table(
    'product_supplier',
    db.Column('product_id', db.Integer, db.ForeignKey('product.product_id'), primary_key=True),
    db.Column('supplier_id', db.Integer, db.ForeignKey('supplier.supplier_id'), primary_key=True)
)


class Stock(db.Model):
    __tablename__ = 'stock'

    stock_id = db.Column(db.Integer, primary_key=True, nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.product_id', ondelete='CASCADE'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String, nullable=False)
    threshold = db.Column(db.Integer, nullable=False)
    product = db.relationship("Product", backref="stocks")


class SupplierOrder(db.Model):
    __tablename__ = 'supplier_order'

    order_id = db.Column(db.Integer, primary_key=True, nullable=False)
    supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.supplier_id', ondelete='CASCADE'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.product_id', ondelete='CASCADE'), nullable=False)
    stock_id = db.Column(db.Integer, db.ForeignKey('stock.stock_id', ondelete='CASCADE'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Numeric(10, 2), nullable=False)
    order_date = db.Column(db.DateTime, nullable=False)
    
    supplier = db.relationship("Supplier", backref=db.backref("supplier_orders", cascade="all, delete-orphan"))
    product = db.relationship("Product", backref=db.backref("supplier_orders", cascade="all, delete-orphan"))
    stock = db.relationship("Stock", backref=db.backref("supplier_orders", cascade="all, delete-orphan"))

    def calculate_total_price(self):
        if self.product:
            self.total_price = self.quantity * self.product.price




class SupplierTransaction(db.Model):
    __tablename__ = 'supplier_transaction'

    transaction_id = db.Column(db.Integer, primary_key=True, nullable=False)
    supplier_id = db.Column(db.Integer, db.ForeignKey('supplier.supplier_id', ondelete='CASCADE'), nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey('supplier_order.order_id', ondelete='CASCADE'), nullable=False)
    amount = db.Column(db.Numeric(10, 2), nullable=False)
    transaction_date = db.Column(db.DateTime, nullable=False)

    supplier = db.relationship("Supplier", backref=db.backref("transactions", cascade="all, delete-orphan"))
    order = db.relationship("SupplierOrder", backref=db.backref("transactions", cascade="all, delete-orphan"))


class Consumer(db.Model):
    __tablename__ = 'consumer'

    consumer_id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String, nullable=False)
    contact = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)

class ConsumerOrder(db.Model):
    __tablename__ = 'consumer_order'

    order_id = db.Column(db.Integer, primary_key=True, nullable=False)
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

class ConsumerTransaction(db.Model):
    __tablename__ = 'consumer_transaction'

    transaction_id = db.Column(db.Integer, primary_key=True, nullable=False)
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