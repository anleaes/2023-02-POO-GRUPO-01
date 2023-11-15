from client import Client

class Order:

    def __init__(self, total_price, status, client = Client):
        self._total_price = total_price
        self._status = status
        self._client = client

    def getOrderDetail(self):
        print("------------Order details------------")
        print(f"Total price: {self._total_price} \nStatus: {self._status}\n")