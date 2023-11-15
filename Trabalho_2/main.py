from client import Client
from social_network import SocialNetwork

from client_social_network import ClientSocialNetwork

from category import Category
from product import Product

from order import Order
from order_item import OrderItem

def main():

    client = Client('Nome', 'Completo', 'Rua A, 123', '(51) 99999.9999', 'teste@teste.com', 'masculino')
    socialNetwork = SocialNetwork('Social 1', 'Descrição 1')
    clientSocialNetwork = ClientSocialNetwork(client, socialNetwork)

    category = Category(1, 'Categoria 1', 'Descrição 1')
    product = Product('Produto 1', 'Descrição 1', '01/01/2023', True, category)

    order = Order(100, 'Finalizado', client)
    orderItem = OrderItem(10, 10, order, product)


    clientSocialNetwork.exibirClientSocialNetwork()
    product.getProductDetails()
    order.getOrderDetail()
    orderItem.getOrderItemDetail()


if __name__ == "__main__":
    main()