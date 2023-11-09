class OrderItem:

    def __init__(self, quantity, unitary_price, order, product):
        self._quantity = quantity
        self._unitary_price = unitary_price
        self._order = order
        self._product = product