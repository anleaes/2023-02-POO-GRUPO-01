from client import Client
from social_network import SocialNetwork

class ClientSocialNetwork:

    def __init__(self, client, socialNetwork):
        self._client = client
        self._socialNetwork = socialNetwork

    def exibirClientSocialNetwork(self):
        print('------------Client SocialNetwork------------')
        print(f"Client: {self._client.getFirstName()}\nSocialNetwork: {self._socialNetwork.getSocialDescription()}\n")