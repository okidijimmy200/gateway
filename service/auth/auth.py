from typing import Tuple
from service.interface import AuthProvider
from models.models.user_models import LoginRequest, ValidateTokenRequest, ValidateTokenResponse

class Auth:
    auth_provider: AuthProvider

    def __init__(self, auth_provider: AuthProvider):
        self.auth_provider = auth_provider

    def login(self, request: LoginRequest) -> Tuple[int, str]:
        '''login user'''
        return self.auth_provider.login(request)

    def validate_token(self, request: ValidateTokenRequest) -> ValidateTokenResponse:
        '''validate token generated'''
        return self.auth_provider.validate_token(request)