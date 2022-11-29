from service.interface import ClientInterface

class ClientManagmentService:
    def __init__(self, client_service: ClientInterface) -> None:
        self.client_service = client_service

    def run(self):
        self.client_service.connect()



