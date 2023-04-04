from server.http.server import get_app
from provider.auth.auth import Auth, Token
from provider.register.register import Register
from provider.api.api import SportsBet 
from server.http.middleware.middleware import TokenRequiredService
from service.auth.auth import Auth as AuthService
from service.registration.registration import Registration as RegistrationService
from service.api.api import SportBet as SportBetService


if __name__ == '__main__':
    app = get_app(
        AuthService(Auth()),
        RegistrationService(Register()),
        SportBetService(SportsBet()),
        TokenRequiredService(Token())
        )
    app.run(host="localhost", port=8000, debug=True)