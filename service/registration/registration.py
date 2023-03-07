from typing import Tuple
from service.interface import RegistrationProvider
from models.models.user_models import (
    SignUpRequest,
    SignUpResponse
)

class Registration:
    registration_provider: RegistrationProvider

    def __init__(self, registration_provider: RegistrationProvider):
        self.registration_provider = registration_provider

    def signup(self, request: SignUpRequest) -> SignUpResponse:
        '''signup user'''
        return self.registration_provider.signup(request)


