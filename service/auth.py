from service.interface import AuthProvider
from models.user_models import LoginRequest, ValidateTokenRequest, ValidateTokenResponse, LoginResponse


class AuthService():
    auth_provider: AuthProvider

    def __init__(self, auth_provider: AuthProvider):
        self.auth_provider = auth_provider

    def login(self, request: LoginRequest) -> LoginResponse:
        '''login user'''
        return self.auth_provider.login(request)

    def validate_token(self, request: ValidateTokenRequest) -> ValidateTokenResponse:
        '''validate user token'''
        return self.auth_provider.validate_token(request)
