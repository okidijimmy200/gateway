from abc import ABC, abstractmethod
from typing import Tuple
from models.models.user_models import (
    SignUpRequest,
    SignUpResponse,
    LoginRequest,
    ValidateTokenRequest,
    ValidateTokenResponse,
    
)
from models.models.sportbet_models import (
    CreateBetRequest,
    CreateBetResponse,
    ReadBetRequest,
    ReadBetResponse,
    UpdateBetRequest,
    UpdateBetResponse,
    DeleteBetRequest,
    DeleteBetResponse
)

class AuthService(ABC):
    '''Auth Service methods'''
    @abstractmethod
    def login(self, request: LoginRequest) -> Tuple[int, str]:
        pass

    @abstractmethod
    def validate_token(self, req: ValidateTokenRequest) -> ValidateTokenResponse:
        pass

class RegistrationService(ABC):
    @abstractmethod
    def signup(self, req: SignUpRequest) -> SignUpResponse:
        pass

class SportbetService(ABC):
    @abstractmethod
    def create(self, req: CreateBetRequest) -> CreateBetResponse:
        pass

    @abstractmethod
    def read(self, req: ReadBetRequest) -> ReadBetResponse:
        pass

    @abstractmethod
    def update(self, req: UpdateBetRequest) -> UpdateBetResponse:
        pass

    @abstractmethod
    def delete(self, req: DeleteBetRequest) -> DeleteBetResponse:
        pass


class AuthProvider(ABC):
    '''Auth provider methods'''
    @abstractmethod
    def login(self, request: LoginRequest) -> Tuple[int, str]:
        pass

    @abstractmethod
    def validate_token(self, req: ValidateTokenRequest) -> ValidateTokenResponse:
        pass

class RegistrationProvider(ABC):
    @abstractmethod
    def signup(self, req: SignUpRequest) -> SignUpResponse:
        pass

class RegistrationService(ABC):
    @abstractmethod
    def signup(self, req: SignUpRequest) -> SignUpResponse:
        pass

class SportbetProvider(ABC):
    @abstractmethod
    def create(self, req: CreateBetRequest) -> CreateBetResponse:
        pass

    @abstractmethod
    def read(self, req: ReadBetRequest) -> ReadBetResponse:
        pass

    @abstractmethod
    def update(self, req: UpdateBetRequest) -> UpdateBetResponse:
        pass

    @abstractmethod
    def delete(self, req: DeleteBetRequest) -> DeleteBetResponse:
        pass