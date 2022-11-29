from google.protobuf.json_format import MessageToJson
from flask import  request
from flask import Blueprint, jsonify
from middleware.middleware import token_required
from server.grpc.grpc import SportsBet

sport_bet = Blueprint('sport_bet', __name__)

@sport_bet.route('/createbet', methods=['POST'])
@token_required
def create_bet(current_user):
    try:
        if current_user:
            data = request.get_json()
            create_bet_client = SportsBet()
            response = create_bet_client.create_bet(
                league=data['league'],
                home_team=data['home_team'],
                away_team=data['away_team'],
                home_team_win_odds=data['home_team_win_odds'],
                away_team_win_odds=data['away_team_win_odds'],
                draw_odds=data['draw_odds'],
                game_date=data['game_date']
                )
            print(response.code)
            reason = {
                "code": response.code,
                "reason": response.reason
            }
            # print(response)
            return jsonify(reason)

    except Exception as e:
        result = (
                f"-Error "
                + f"{type(e).__name__} {str(e)}"
            )
        print(result)
        return result

@sport_bet.route('/readbet', methods=['GET'])
@token_required
def read_bet(current_user):
    try:
        if current_user:
            data = {
            "league": f"{request.args.to_dict()['league']}",
            "start_date": f"{request.args.to_dict()['start_date']}",
            "end_date": f"{request.args.to_dict()['end_date']}"
        }
            read_bet_client = SportsBet()
            response =  read_bet_client.read_bet(league=data['league'], start_date=data['start_date'], end_date=data["end_date"])
            reason = {
                "code": response.code,
                "response": response.response,
                "reason": response.reason
            }
            # print(response)
            serialized = MessageToJson(response)
            print(serialized)
            return serialized
    except Exception as e:
        result = (
                f"-Error "
                + f"{type(e).__name__} {str(e)}"
            )
        print(result)
        return result

    