from flask import Flask
from routers.auth_router import auth_api
from routers.registration_router import registration_api
from routers.bet_router import sport_bet
from server.grpc.grpc import ClientManagmentService
from service.flask import FlaskService

app = Flask(__name__) 

app.register_blueprint(registration_api, name='signup')
app.register_blueprint(auth_api, name='auth')
app.register_blueprint(sport_bet, name='sport_bet')

client_server = app.run(host="localhost", port=8000, debug=True)

if __name__ == '__main__':
    flask_service = FlaskService(client_server)
    client_management_service = ClientManagmentService(flask_service)
    client_management_service.run()