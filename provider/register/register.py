import grpc, os
import generated.auth_pb2 as auth_pb2
import generated.auth_pb2_grpc as auth_pb2_grpc

class Register:
    def __init__(self) -> None:
        self.host = os.environ.get('AUTH_SERVICE_HOST')
        self.server_port = os.environ.get('AUTH_SERVICE_PORT')

        self.channel = grpc.insecure_channel(f"{self.host}: {self.server_port}")
        self.stub = auth_pb2_grpc.UserManagenmentServiceStub(self.channel)

    def signup(self, username, email, password):
        signup_request = auth_pb2.SignUpRequest(username=username, email=email, password=password)
        return self.stub.SignUp(signup_request)