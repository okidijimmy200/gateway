import pytest
from unittest.mock import patch
from server.http.server import get_app
from provider.auth.auth import Auth, Token
from provider.register.register import Register
from provider.api.api import SportsBet
from service.auth.auth import Auth as AuthService
from service.registration.registration import Registration as RegistrationService
from service.api.api import SportBet as SportBetService
from server.http.middleware.middleware import TokenRequired


@pytest.fixture
def app():
    flask_app = get_app(
        AuthService(Auth()),
        RegistrationService(Register()),
        SportBetService(SportsBet()),
        TokenRequired(Token())
    )
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()
