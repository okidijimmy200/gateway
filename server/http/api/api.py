from flask import  request
from flask import Blueprint, jsonify
from server.http.middleware.middleware import token_required
from google.protobuf.json_format import MessageToJson
import server.http.server as server
from models.models.sportbet_models import (
    CreateBetRequest,
    UpdateBetRequest,
    ReadBetRequest,
    DeleteBetRequest  
)

sport_bet = Blueprint('sport_bet', __name__)

@sport_bet.route('/createbet', methods=['POST'])
@token_required
def create_bet(current_user):
    try:
        if current_user:
            data: dict = request.get_json()

            # there needs to be isolation of provider from server from everthing
            # except service. (the provider only imports models and service)
            
            req = CreateBetRequest(
                data.get('league'),
                data.get('home_team'),
                data.get('away_team'),
                data.get('home_team_win_odds'),
                data.get('away_team_win_odds'),
                data.get('draw_odds'),
                data.get('game_date'),
                )
            print(req.league)
            response = server.sport_service.create_bet(req)
            # print(response.code)
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
            req = ReadBetRequest(
                request.args.to_dict()['league'],
                request.args.to_dict()['start_date'],
                request.args.to_dict()['end_date']
            )
            response = server.sport_service.read_bet(req)
            return MessageToJson(response)
    except Exception as e:
        result = (
                f"-Error "
                + f"{type(e).__name__} {str(e)}"
            )
        print(result)
        return result

@sport_bet.route('/updatebet/<id>', methods=['PUT'])
@token_required
def update_bet(current_user, id):
    try:
        if current_user:
            data: dict = request.get_json()
            req = UpdateBetRequest(
                id,
                data.get('league'),
                data.get('home_team'),
                data.get('away_team'),
                data.get('home_team_win_odds'),
                data.get('away_team_win_odds'),
                data.get('draw_odds'),
                data.get('game_date'),
            )
            response = server.sport_service.update_bet(req)
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

@sport_bet.route('/deletebet', methods=['DELETE'])    
@token_required  
def delete(current_user):
    try:
        if current_user:
            req = DeleteBetRequest(
                request.args.to_dict()['league'],
                request.args.to_dict()['home_team'],
                request.args.to_dict()['away_team'],
                request.args.to_dict()['game_date']
            )
            response = server.sport_service.delete_bet(req)
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