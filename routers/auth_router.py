import grpc
import generated.auth_pb2 as auth_pb2
import generated.auth_pb2_grpc as auth_pb2_grpc
from flask import  request
from flask import Blueprint, jsonify
from middleware.middleware import token_required

auth_api = Blueprint('auth_api', __name__)


@auth_api.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        with grpc.insecure_channel('0.0.0.0:50052') as channel:
            stub = auth_pb2_grpc.UserManagenmentServiceStub(channel)
            response = stub.Login(auth_pb2.LoginRequest(email=data["email"], password=data["password"]))
            reason = {
                "code": response.code,
                "reason": response.reason,
                "token": response.token
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



