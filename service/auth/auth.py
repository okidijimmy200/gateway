from typing import Tuple
from service.interface import AuthProvider, TokenProvider
from models.models.user_models import LoginRequest, ValidateTokenRequest, ValidateTokenResponse, LoginResponse

class Auth:
    auth_provider: AuthProvider

    def __init__(self, auth_provider: AuthProvider):
        self.auth_provider = auth_provider

    def login(self, request: LoginRequest) -> LoginResponse:
        '''login user'''
        return self.auth_provider.login(request)

