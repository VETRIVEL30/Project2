import unittest

#Supplier table

class Supplier:
    def __init__(self, name, address, contact):
        self.name = name
        self.address = address
        self.contact = contact

    def update_address(self, new_address):
        self.address = new_address

    def update_contact(self, new_contact):
        self.contact = new_contact

class StockTest(unittest.TestCase):
    def test_init(self):
        supplier = Supplier("Vetri", "Chennai", 8765456789)
        self.assertEqual(supplier.name, "Vetri")
        self.assertEqual(supplier.address, "Chennai")
        self.assertEqual(supplier.contact, 8765456789)

    def test_update_address(self):
        supplier = Supplier("Vetri", "Chennai", 8765456789)
        supplier.update_address("Bangalore")
        self.assertEqual(supplier.address, "Bangalore")

    def test_update_contact(self):
        supplier = Supplier("Vetri", "Chennai", 8765456789)
        supplier.update_contact(9767564534)
        self.assertEqual(supplier.contact, 9767564534)

#Product table

class Product:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

class ProductTest(unittest.TestCase):
    def test_init(self):
        product = Product("iPhone", "Smartphone", 1000)
        self.assertEqual(product.name, "iPhone")
        self.assertEqual(product.description, "Smartphone")
        self.assertEqual(product.price, 1000)

#Stock Table 
 
class Stock:
    def __init__(self, product_id, quantity, location):
        self.product_id = product_id
        self.quantity = quantity
        self.location = location

class StockTest(unittest.TestCase):
    def test_init(self):
        stock = Stock(1234, 10, "Warehouse A")
        self.assertEqual(stock.product_id, 1234)
        self.assertEqual(stock.quantity, 10)
        self.assertEqual(stock.location, "Warehouse A")

#Supplier_order table

class SupplierOrder:
    def __init__(self, product_id, supplier_id, stock_id, quantity, total_price, order_date):
        self.product_id = product_id
        self.supplier_id = supplier_id
        self.stock_id = stock_id
        self.quantity = quantity
        self.total_price = total_price
        self.order_date = order_date

class SupplierOrderTest(unittest.TestCase):
    def test_init(self):
        supplier_order = SupplierOrder(1234, 5678, 9876, 5, 2500, "2023-07-07")
        self.assertEqual(supplier_order.product_id, 1234)
        self.assertEqual(supplier_order.supplier_id, 5678)
        self.assertEqual(supplier_order.stock_id, 9876)
        self.assertEqual(supplier_order.quantity, 5)
        self.assertEqual(supplier_order.total_price, 2500)
        self.assertEqual(supplier_order.order_date, "2023-07-07")


#Supplier_transaction table

class SupplierTransaction:
    def __init__(self, supplier_id, order_id, amount, transaction_date):
        self.supplier_id = supplier_id
        self.order_id = order_id
        self.amount = amount
        self.transaction_date = transaction_date

class SupplierTransactionTest(unittest.TestCase):
    def test_init(self):
        supplier_transaction = SupplierTransaction(1234, 5678, 2000, "2023-07-07")
        self.assertEqual(supplier_transaction.supplier_id, 1234)
        self.assertEqual(supplier_transaction.order_id, 5678)
        self.assertEqual(supplier_transaction.amount, 2000)
        self.assertEqual(supplier_transaction.transaction_date, "2023-07-07")

#Consumer table

class Consumer:
    def __init__(self, name, address, contact):
        self.name = name
        self.address = address
        self.contact = contact

class ConsumerTest(unittest.TestCase):
    def test_init(self):
        consumer = Consumer("Muthu", "Madurai", 1234567890)
        self.assertEqual(consumer.name, "Muthu")
        self.assertEqual(consumer.address, "Madurai")
        self.assertEqual(consumer.contact, 1234567890)

#Consumer_order table

class ConsumerOrder:
    def __init__(self, consumer_id, product_id, quantity, total_price, order_date):
        self.consumer_id = consumer_id
        self.product_id = product_id
        self.quantity = quantity
        self.total_price = total_price
        self.order_date = order_date

class ConsumerOrderTest(unittest.TestCase):
    def test_init(self):
        consumer_order = ConsumerOrder(1234, 5678, 2, 2000, "2023-07-07")
        self.assertEqual(consumer_order.consumer_id, 1234)
        self.assertEqual(consumer_order.product_id, 5678)
        self.assertEqual(consumer_order.quantity, 2)
        self.assertEqual(consumer_order.total_price, 2000)
        self.assertEqual(consumer_order.order_date, "2023-07-07")

#Consumer_transaction table

class ConsumerTransaction:
    def __init__(self, consumer_id, order_id, stock_id, amount, transaction_date):
        self.consumer_id = consumer_id
        self.order_id = order_id
        self.stock_id = stock_id
        self.amount = amount
        self.transaction_date = transaction_date

class ConsumerTransactionTest(unittest.TestCase):
    def test_init(self):
        consumer_transaction = ConsumerTransaction(1234, 5678, 9876, 2000, "2023-07-07")
        self.assertEqual(consumer_transaction.consumer_id, 1234)
        self.assertEqual(consumer_transaction.order_id, 5678)
        self.assertEqual(consumer_transaction.stock_id, 9876)
        self.assertEqual(consumer_transaction.amount, 2000)
        self.assertEqual(consumer_transaction.transaction_date, "2023-07-07")


if __name__ == "__main__":
    unittest.main()
