import re

from models import *
from sqlalchemy.exc import SQLAlchemyError


class SupplierDAO:
    EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    CONTACT_REGEX = r'^\+?\d+$'

    @staticmethod
    def validate_email(email):
        return bool(re.match(SupplierDAO.EMAIL_REGEX, email))

    @staticmethod
    def validate_contact(contact):
        return bool(re.match(SupplierDAO.CONTACT_REGEX, contact))

    @staticmethod
    def create_supplier(name, address, contact, email):
        try:
            if not SupplierDAO.validate_email(email):
                raise ValueError("Invalid email format")
            if not SupplierDAO.validate_contact(contact):
                raise ValueError("Invalid contact number format")

            supplier = Supplier(name=name, address=address, contact=contact, email=email)
            db.session.add(supplier)
            db.session.commit()
            return supplier
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e
        finally:
            db.session.close()

    @staticmethod
    def get_supplier_by_id(supplier_id):
        return Supplier.query.get(supplier_id)

    @staticmethod
    def get_all_suppliers():
        return Supplier.query.all()

    @staticmethod
    def update_supplier(supplier_id, name=None, address=None, contact=None, email=None):
        try:
            supplier = SupplierDAO.get_supplier_by_id(supplier_id)
            if supplier:
                if name:
                    supplier.name = name
                if address:
                    supplier.address = address
                if contact:
                    if not SupplierDAO.validate_contact(contact):
                        raise ValueError("Invalid contact number format")
                    supplier.contact = contact
                if email:
                    if not SupplierDAO.validate_email(email):
                        raise ValueError("Invalid email format")
                    supplier.email = email
                db.session.commit()
            return supplier
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e
        finally:
            db.session.close()

    @staticmethod
    def delete_supplier(supplier_id):
        try:
            supplier = SupplierDAO.get_supplier_by_id(supplier_id)
            if supplier:
                db.session.delete(supplier)
                db.session.commit()
            return supplier
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e
        finally:
            db.session.close()

# ==========================================product===========================================================================================================================
class ProductDAO:
    @staticmethod
    def create_product(name, description, price):
        try:
            product = Product(name=name, description=description, price=price)
            db.session.add(product)
            db.session.commit()
            return product
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e
        finally:
            db.session.close()

    @staticmethod
    def get_product_by_id(product_id):
        return Product.query.get(product_id)

    @staticmethod
    def get_all_products():
        return Product.query.all()

    @staticmethod
    def update_product(product_id, name=None, description=None, price=None):
        try:
            product = ProductDAO.get_product_by_id(product_id)
            if product:
                if name:
                    product.name = name
                if description:
                    product.description = description
                if price:
                    product.price = price
                db.session.commit()
            return product
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e
        finally:
            db.session.close()

    @staticmethod
    def delete_product(product_id):
        try:
            product = ProductDAO.get_product_by_id(product_id)
            if product:
                db.session.delete(product)
                db.session.commit()
            return product
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e
        finally:
            db.session.close()

# ==============================================STOCK=====================================================================================================================

class StockDAO:
    @staticmethod
    def create_stock(product_id, quantity, location, threshold):
        try:
            product = ProductDAO.get_product_by_id(product_id)
            if product:
                stock = Stock(product=product, quantity=quantity, location=location, threshold=threshold)
                db.session.add(stock)
                db.session.commit()
                return stock
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e
        finally:
            db.session.close()

    @staticmethod
    def get_stock_by_id(stock_id):
        return Stock.query.get(stock_id)

    @staticmethod
    def get_stock_by_product_id(product_id):
        return Stock.query.filter_by(product_id=product_id).first()

    @staticmethod
    def get_all_stocks():
        return Stock.query.all()

    @staticmethod
    def update_stock(stock_id, quantity=None, location=None, threshold=None):
        try:
            stock = StockDAO.get_stock_by_id(stock_id)
            if stock:
                if quantity is not None:
                    stock.quantity = quantity
                if location:
                    stock.location = location
                if threshold is not None:
                    stock.threshold = threshold
                db.session.commit()
            return stock
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e
        finally:
            db.session.close()

    @staticmethod
    def delete_stock(stock_id):
        try:
            stock = StockDAO.get_stock_by_id(stock_id)
            if stock:
                db.session.delete(stock)
                db.session.commit()
            return stock
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e
        finally:
            db.session.close()

# ================================================================================SDAO========================================================================================
class SupplierOrderDAO:
    @staticmethod
    def create_supplier_order(supplier_id, product_id, stock_id, quantity, order_date):
        try:
            supplier = SupplierDAO.get_supplier_by_id(supplier_id)
            product = ProductDAO.get_product_by_id(product_id)
            stock = StockDAO.get_stock_by_id(stock_id)
            if supplier and product and stock:
                total_price = quantity * product.price
                supplier_order = SupplierOrder(
                    supplier=supplier,
                    product=product,
                    stock=stock,
                    quantity=quantity,
                    total_price=total_price,
                    order_date=order_date
                )
                db.session.add(supplier_order)
                db.session.commit()

                stock.quantity += quantity
                db.session.commit()
                return supplier_order
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e
        finally:
            db.session.close()

    @staticmethod
    def get_orders_by_supplier_id(supplier_id):
        return SupplierOrder.query.filter_by(supplier_id=supplier_id).all()

    @staticmethod
    def get_suppliers_by_order_id(order_id):
        return Supplier.query.join(SupplierOrder).filter(SupplierOrder.order_id == order_id).all()

    @staticmethod
    def get_supplier_order_by_id(order_id):
        return SupplierOrder.query.get(order_id)

    @staticmethod
    def get_all_supplier_orders():
        return SupplierOrder.query.all()

    @staticmethod
    def update_supplier_order(order_id, quantity=None, order_date=None):
        try:
            order = SupplierOrderDAO.get_supplier_order_by_id(order_id)
            if order:
                if quantity is not None:
                    previous_quantity = order.quantity
                    order.quantity = quantity
                if order_date is not None:
                    order.order_date = order_date
                order.calculate_total_price()
                db.session.commit()

                stock = order.stock
                if stock and quantity is not None and previous_quantity is not None:
                    quantity_change = quantity - previous_quantity

                    stock.quantity += quantity_change
                    db.session.commit()

            return order
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e
        finally:
            db.session.close()

    @staticmethod
    def delete_supplier_order(order_id):
        try:
            order = SupplierOrderDAO.get_supplier_order_by_id(order_id)
            if order:
                stock = order.stock
                if stock:
                    stock.quantity -= order.quantity
                    db.session.commit()

                db.session.delete(order)
                db.session.commit()

            return order
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e
        finally:
            db.session.close()

# =====================================================================================================consumer==============================================================================
class ConsumerDAO:
    EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    CONTACT_REGEX = r'^\+?\d+$'

    @staticmethod
    def validate_email(email):
        return bool(re.match(ConsumerDAO.EMAIL_REGEX, email))

    @staticmethod
    def validate_contact(contact):
        return bool(re.match(ConsumerDAO.CONTACT_REGEX, contact))

    @staticmethod
    def create_consumer(name, address, contact, email):
        try:
            if not ConsumerDAO.validate_email(email):
                raise ValueError("Invalid email format")
            if not ConsumerDAO.validate_contact(contact):
                raise ValueError("Invalid contact number format")

            consumer = Consumer(name=name, address=address, contact=contact, email=email)
            db.session.add(consumer)
            db.session.commit()
            return consumer
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e
        finally:
            db.session.close()

    @staticmethod
    def get_consumer_by_id(consumer_id):
        return Consumer.query.get(consumer_id)

    @staticmethod
    def get_all_consumers():
        return Consumer.query.all()

    @staticmethod
    def update_consumer(consumer_id, name=None, address=None, contact=None, email=None):
        try:
            consumer = ConsumerDAO.get_consumer_by_id(consumer_id)
            if consumer:
                if name:
                    consumer.name = name
                if address:
                    consumer.address = address
                if contact:
                    if not ConsumerDAO.validate_contact(contact):
                        raise ValueError("Invalid contact number format")
                    consumer.contact = contact
                if email:
                    if not ConsumerDAO.validate_email(email):
                        raise ValueError("Invalid email format")
                    consumer.email = email
                db.session.commit()
            return consumer
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e
        finally:
            db.session.close()

    @staticmethod
    def delete_consumer(consumer_id):
        try:
            consumer = ConsumerDAO.get_consumer_by_id(consumer_id)
            if consumer:
                db.session.delete(consumer)
                db.session.commit()
            return consumer
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e
        finally:
            db.session.close()

# ==========================================================================================CSDAO=====================================================================================================================================

class ConsumerOrderDAO:
    @staticmethod
    def create_consumer_order(consumer_id, product_id, quantity, order_date):
        try:
            consumer = ConsumerDAO.get_consumer_by_id(consumer_id)
            product = ProductDAO.get_product_by_id(product_id)
            if consumer and product:
                consumer_order = ConsumerOrder(
                    consumer=consumer,
                    product=product,
                    quantity=quantity,
                    order_date=order_date
                )
                consumer_order.calculate_total_price()
                db.session.add(consumer_order)
                db.session.commit()

                stock = StockDAO.get_stock_by_product_id(product_id)
                if stock:
                    if quantity > stock.quantity or stock.quantity <= stock.threshold:
                        remaining_quantity = max(quantity - stock.quantity, 0)
                        SupplierOrderDAO.create_supplier_order(
                            supplier_id=stock.product.supplier_id,
                            product_id=product_id,
                            stock_id=stock.id,
                            quantity=remaining_quantity,
                            order_date=order_date
                        )

                stock = StockDAO.get_stock_by_product_id(product_id)
                if stock:
                    if stock.quantity >= quantity:
                        stock.quantity -= quantity
                        db.session.commit()
                    else:
                        raise ValueError("Insufficient stock quantity")

                return consumer_order
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e
        finally:
            db.session.close()

    @staticmethod
    def get_consumer_order_by_id(order_id):
        try:
            return ConsumerOrder.query.get(order_id)
        except SQLAlchemyError as e:
            raise e

    @staticmethod
    def get_all_consumer_orders():
        try:
            return ConsumerOrder.query.all()
        except SQLAlchemyError as e:
            raise e

    @staticmethod
    def get_orders_by_consumer_id(consumer_id):
        try:
            return ConsumerOrder.query.filter_by(consumer_id=consumer_id).all()
        except SQLAlchemyError as e:
            raise e

    @staticmethod
    def get_consumers_by_order_id(order_id):
        try:
            return Consumer.query.join(ConsumerOrder).filter(ConsumerOrder.order_id == order_id).all()
        except SQLAlchemyError as e:
            raise e

    @staticmethod
    def update_consumer_order(order_id, quantity=None, order_date=None):
        try:
            order = ConsumerOrderDAO.get_consumer_order_by_id(order_id)
            if order:
                if quantity is not None:
                    previous_quantity = order.quantity
                    order.quantity = quantity
                if order_date is not None:
                    order.order_date = order_date
                order.calculate_total_price()
                db.session.commit()

                stock = StockDAO.get_stock_by_product_id(order.product_id)
                if stock and quantity is not None and previous_quantity is not None:
                    quantity_change = quantity - previous_quantity

                    if quantity_change > 0:
                        if quantity_change > stock.quantity or stock.quantity <= stock.threshold:
                            remaining_quantity = max(quantity_change - stock.quantity, 0)
                            SupplierOrderDAO.create_supplier_order(
                                supplier_id=stock.product.supplier_id,
                                product_id=order.product_id,
                                stock_id=stock.id,
                                quantity=remaining_quantity,
                                order_date=order.order_date
                            )
                    elif quantity_change < 0:
                        SupplierOrderDAO.delete_supplier_order_by_product_and_order(
                            product_id=order.product_id,
                            consumer_order_id=order.id
                        )

                stock = StockDAO.get_stock_by_product_id(order.product_id)
                if stock and quantity is not None and previous_quantity is not None:
                    quantity_change = quantity - previous_quantity

                    if quantity_change > 0:
                        if stock.quantity >= quantity_change:
                            stock.quantity -= quantity_change
                        else:
                            raise ValueError("Insufficient stock quantity")
                    elif quantity_change < 0:
                        stock.quantity -= abs(quantity_change)

                    db.session.commit()

            return order
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e
        finally:
            db.session.close()

    @staticmethod
    def delete_consumer_order(order_id):
        try:
            order = ConsumerOrderDAO.get_consumer_order_by_id(order_id)
            if order:
                SupplierOrderDAO.delete_supplier_order_by_product_and_order(
                    product_id=order.product_id,
                    consumer_order_id=order.id
                )

                stock = StockDAO.get_stock_by_product_id(order.product_id)
                if stock:
                    stock.quantity += order.quantity
                    db.session.commit()

                db.session.delete(order)
                db.session.commit()
            return order
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e
        finally:
            db.session.close()
# =======================================================================================================ConsumerTransaction================================================================

class ConsumerTransactionDAO:
    @staticmethod
    def create_consumer_transaction(consumer_id, order_id, transaction_date):
        try:
            consumer = ConsumerDAO.get_consumer_by_id(consumer_id)
            order = ConsumerOrderDAO.get_consumer_order_by_id(order_id)
            if consumer and order:
                transaction = ConsumerTransaction(
                    consumer=consumer,
                    order=order,
                    transaction_date=transaction_date
                )
                transaction.amount = order.total_price
                db.session.add(transaction)
                db.session.commit()
                return transaction
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e
        finally:
            db.session.close()

    @staticmethod
    def get_transactions_by_consumer_id(consumer_id):
        try:
            return ConsumerTransaction.query.filter_by(consumer_id=consumer_id).all()
        except SQLAlchemyError as e:
            raise e

    @staticmethod
    def get_consumer_by_transaction_id(transaction_id):
        try:
            transaction = ConsumerTransaction.query.get(transaction_id)
            if transaction:
                return transaction.consumer
            return None
        except SQLAlchemyError as e:
            raise e

    @staticmethod
    def get_order_by_transaction_id(transaction_id):
        try:
            transaction = ConsumerTransaction.query.get(transaction_id)
            if transaction:
                return transaction.order
            return None
        except SQLAlchemyError as e:
            raise e

    @staticmethod
    def get_transaction_by_order_id(order_id):
        try:
            return ConsumerTransaction.query.filter_by(order_id=order_id).first()
        except SQLAlchemyError as e:
            raise e

    @staticmethod
    def update_consumer_transaction(transaction_id, transaction_date=None):
        try:
            transaction = ConsumerTransaction.query.get(transaction_id)
            if transaction:
                if transaction_date:
                    transaction.transaction_date = transaction_date
                db.session.commit()
            return transaction
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e
        finally:
            db.session.close()

    @staticmethod
    def delete_consumer_transaction(transaction_id):
        try:
            transaction = ConsumerTransaction.query.get(transaction_id)
            if transaction:
                db.session.delete(transaction)
                db.session.commit()
            return transaction
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e
        finally:
            db.session.close()

# ====================================================================SupplierTransaction==============================================================================================================================================================================
class SupplierTransactionDAO:
    @staticmethod
    def get_transactions_by_supplier_id(supplier_id):
        try:
            return SupplierTransaction.query.filter_by(supplier_id=supplier_id).all()
        except SQLAlchemyError as e:
            raise e

    @staticmethod
    def get_supplier_by_transaction_id(transaction_id):
        try:
            transaction = SupplierTransaction.query.get(transaction_id)
            if transaction:
                return transaction.supplier
            return None
        except SQLAlchemyError as e:
            raise e

    @staticmethod
    def get_order_by_transaction_id(transaction_id):
        try:
            transaction = SupplierTransaction.query.get(transaction_id)
            if transaction:
                return transaction.order
            return None
        except SQLAlchemyError as e:
            raise e

    @staticmethod
    def get_transaction_by_order_id(order_id):
        try:
            return SupplierTransaction.query.filter_by(order_id=order_id).first()
        except SQLAlchemyError as e:
            raise e

    @staticmethod
    def create_supplier_transaction(supplier_id, order_id, transaction_date):
        try:
            supplier = SupplierDAO.get_supplier_by_id(supplier_id)
            order = SupplierOrderDAO.get_supplier_order_by_id(order_id)
            if supplier and order:
                transaction = SupplierTransaction(
                    supplier=supplier,
                    order=order,
                    transaction_date=transaction_date
                )
                transaction.amount = order.total_price
                db.session.add(transaction)
                db.session.commit()
                return transaction
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e
        finally:
            db.session.close()

    @staticmethod
    def get_supplier_transaction_by_id(transaction_id):
        try:
            return SupplierTransaction.query.get(transaction_id)
        except SQLAlchemyError as e:
            raise e

    @staticmethod
    def get_all_supplier_transactions():
        try:
            return SupplierTransaction.query.all()
        except SQLAlchemyError as e:
            raise e

    @staticmethod
    def update_supplier_transaction(transaction_id, transaction_date=None):
        try:
            transaction = SupplierTransaction.query.get(transaction_id)
            if transaction:
                if transaction_date:
                    transaction.transaction_date = transaction_date
                db.session.commit()
            return transaction
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e
        finally:
            db.session.close()

    @staticmethod
    def delete_supplier_transaction(transaction_id):
        try:
            transaction = SupplierTransaction.query.get(transaction_id)
            if transaction:
                db.session.delete(transaction)
                db.session.commit()
            return transaction
        except SQLAlchemyError as e:
            db.session.rollback()
            raise e
        finally:
            db.session.close()
