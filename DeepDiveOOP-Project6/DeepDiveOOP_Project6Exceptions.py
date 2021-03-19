from datetime import datetime

class WidgetException(Exception):
    message = "Generic Widget exception."

    def __init__(self, *args, customer_message=None):
        super().__init__(args)
        if args:
            self.message = args[0]
        self.customer_message = customer_message if customer_message is not None else self.message

    def log_exception(self):
        exception = {
            "type": type(self).__name__,
            "message": self.message,
            "args": self.args[1:]
        }
        print(f"Exception: {datetime.utcnow().isoformat()}: {exception}")

# ex1 = WidgetException('some custom message', 10, 100)

# ex1.log_exception()

class SupplierException(WidgetException):
    message = "Supplier exception"

class NotManufacturedException(SupplierException):
    message = "Widget is no longer manufactured by supplier"

class ProductionDelayedException(SupplierException):
    message = "Widget production has been delayed by manufacturer"

class ShippingDelayedException(SupplierException):
    message = "Widget shipping has been delayed by supplier"

class CheckoutException(WidgetException):
    messsage = "Checkout inventory exception"

try:
    raise SupplierException()
except SupplierException as ex:
    ex.log_exception()
    raise
