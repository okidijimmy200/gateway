from service.interface import ClientInterface

class FlaskService(ClientInterface):
    def __init__(self, client_service) -> None:
        self.client_service = client_service

    def connect(self):
        self.client_service