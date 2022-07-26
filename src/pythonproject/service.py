from pythonproject.client import Client


class Service:
    client: Client

    def __init__(self, client: Client):
        self.client = Client() if client is None else client

    def hello(self):
        return self.client.doPost()
