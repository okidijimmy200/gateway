import os
from flask import Flask
from service.interface import AuthService, RegistrationService, SportbetService, TokenService
from server.http.auth.auth import auth_api
from server.http.register.register import registration_api


auth_service: AuthService
reg_service: RegistrationService
sport_service: SportbetService
token_service: TokenService

def get_app(
    auth: AuthService, 
    reg: RegistrationService,
    sport: SportbetService,
    token: TokenService  
    ):
    app = Flask(__name__)

    global auth_service, reg_service, sport_service, token_service
    auth_service = auth
    reg_service  = reg
    sport_service = sport
    token_service = token

    import server.http.api.api as sport_bet

    app.register_blueprint(auth_api, name='auth')
    app.register_blueprint(registration_api, name='register')
    app.register_blueprint(sport_bet.sport_bet, name='api')

    return app