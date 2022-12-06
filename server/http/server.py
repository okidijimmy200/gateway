import os
from flask import Flask
from service.interface import AuthService, RegistrationService, SportbetService
from server.http.auth.auth import auth_api
from server.http.register.register import registration_api
from server.http.api.api import sport_bet

auth_service: AuthService
reg_service: RegistrationService
sport_service: SportbetService

def get_app(
    auth: AuthService, 
    reg: RegistrationService,
    sport: SportbetService
    ):
    app = Flask(__name__)

    global auth_service, reg_service, sport_service
    auth_service = auth
    reg_service  = reg
    sport_service = sport

    app.register_blueprint(auth_api, name='auth')
    app.register_blueprint(registration_api, name='register')
    app.register_blueprint(sport_bet, name='api')

    return app