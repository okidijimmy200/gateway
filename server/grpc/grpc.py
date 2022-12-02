import grpc, os
import generated.auth_pb2 as auth_pb2
import generated.auth_pb2_grpc as auth_pb2_grpc
import generated.sportbet_pb2 as sportbet_pb2
import generated.sportbet_pb2_grpc as sportbet_pb2_grpc
from service.interface import ClientInterface

class AuthClient:
    def __init__(self) -> None:
        self.host = os.environ.get('AUTH_SERVICE_HOST')
        self.server_port = os.environ.get('AUTH_SERVICE_PORT')

        self.channel = grpc.insecure_channel(f"{self.host}: {self.server_port}")
        self.stub = auth_pb2_grpc.UserManagenmentServiceStub(self.channel)

    def signup(self, username, email, password):
        signup_request = auth_pb2.SignUpRequest(username=username, email=email, password=password)
        return self.stub.SignUp(signup_request)

    def login(self, email, password):
        login_request = auth_pb2.LoginRequest(email=email, password=password)
        return self.stub.Login(login_request)

    def token(self, token):
        token_required = auth_pb2.ValidateTokenRequest(token=token)
        return self.stub.ValidateToken(token_required)

class SportsBet:
    def __init__(self) -> None:
        self.host = os.environ.get('BET_SERVICE_HOST')
        self.server_port = os.environ.get('BET_SERVICE_PORT')

        self.channel = grpc.insecure_channel(f"{self.host}: {self.server_port}")
        self.stub = sportbet_pb2_grpc.SportBetManagementServiceStub(self.channel)

    def create_bet(self, league, home_team, away_team, home_team_win_odds, away_team_win_odds,draw_odds, game_date):
        bet_request = sportbet_pb2.CreateBetRequest(
            league=league,
            home_team=home_team,
            away_team=away_team,
            home_team_win_odds=home_team_win_odds,
            away_team_win_odds=away_team_win_odds,
            draw_odds=draw_odds,
            game_date=game_date
        )
        return self.stub.CreateBet(bet_request)

    def read_bet(self, league, start_date, end_date):
        read_request = sportbet_pb2.ReadBetRequest(
            league=league,
            start_date=start_date,
            end_date=end_date
        )
        return self.stub.ReadBet(read_request)

    def update_bet(self,league, id, home_team, away_team, home_team_win_odds, away_team_win_odds,draw_odds, game_date):
        update_request = sportbet_pb2.UpdateBetRequest(
            id=id,
            league=league,
            home_team=home_team,
            away_team=away_team,
            home_team_win_odds=home_team_win_odds,
            away_team_win_odds=away_team_win_odds,
            draw_odds=draw_odds,
            game_date=game_date
        )
        return self.stub.UpdateBet(update_request)

    def delete_bet(self, league, home_team, away_team, game_date):
        delete_request = sportbet_pb2.DeleteBetRequest(
            league=league,
            home_team=home_team,
            away_team=away_team,
            game_date=game_date
        )
        return self.stub.DeleteBet(delete_request)




class ClientManagmentService:
    def __init__(self, client_service: ClientInterface) -> None:
        self.client_service = client_service

    def run(self):
        self.client_service.connect()



