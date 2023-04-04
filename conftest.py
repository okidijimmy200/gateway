import pytest
from unittest.mock import patch
from server.http.server import get_app
from provider.auth.auth import Auth, Token
from provider.register.register import Register
from provider.api.api import SportsBet 
from service.auth.auth import Auth as AuthService
from service.registration.registration import Registration as RegistrationService
from service.api.api import SportBet as SportBetService
from server.http.middleware.middleware import TokenRequiredService


@pytest.fixture
def app():
    flask_app = get_app(
    AuthService(Auth()),
    RegistrationService(Register()),
    SportBetService(SportsBet()),
    TokenRequiredService(Token())
    )
    yield flask_app
    
@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def unwrap():
    def unwrapper(func):
        if not hasattr(func, '__wrapped__'):
            return func

        return unwrapper(func.__wrapped__)

    yield unwrapper
