from order import Order
from product import Product

class OrderItem:

    def __init__(self, quantity, unitary_price, order = Order, product = Product):
        self._quantity = quantity
        self._unitary_price = unitary_price
        self._order = order
        self._product = product

    def getOrderItemDetail(self):
        print("------------Order item details------------")
        print(f"Quantity: {self._quantity} | Unitary Price: {self._unitary_price} | Product Name: {self._product.getProductName()}\n")