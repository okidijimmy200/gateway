import grpc
import generated.sportbet_pb2 as sportbet_pb2
import generated.sportbet_pb2_grpc as sportbet_pb2_grpc
from flask import  request
from flask import Blueprint, jsonify
from middleware.middleware import token_required

sport_bet = Blueprint('sport_bet', __name__)

@sport_bet.route('/createbet', methods=['POST'])
@token_required
def create_bet(current_user):
    try:
        if current_user:
            data = request.get_json()
            with grpc.insecure_channel('0.0.0.0:50053') as channel:
                stub = sportbet_pb2_grpc.SportBetManagementServiceStub(channel)
                response = stub.CreateBet(sportbet_pb2.CreateBetRequest(**data))
                reason = {
                    "code": response.code,
                    "reason": response.reason
                }
                print(reason)
                return jsonify(reason)

    except Exception as e:
        result = (
                f"-Error "
                + f"{type(e).__name__} {str(e)}"
            )
        print(result)
        return result

    