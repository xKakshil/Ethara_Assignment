class ProductNotFoundError(Exception):
    pass


class CustomerNotFoundError(Exception):
    pass


class OrderNotFoundError(Exception):
    pass


class DuplicateSkuError(Exception):
    pass


class DuplicateEmailError(Exception):
    pass


class InsufficientStockError(Exception):
    pass