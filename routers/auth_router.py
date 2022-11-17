import grpc
import auth_pb2, auth_pb2_grpc
from flask import  request
from flask import Blueprint, jsonify

auth_api = Blueprint('auth_api', __name__)

'''schema for user model'''


'''signup user'''
@auth_api.route('/signup', methods = ['POST'])
def signup():
    try:
        data = request.get_json()
        with grpc.insecure_channel('0.0.0.0:50052') as channel:
            stub = auth_pb2_grpc.SignUpServiceStub(channel)
            response = stub.signUp(auth_pb2.SignUpRequest(username=data["username"], email=data["email"], password=data["password"]))
            reason = {
                "username": response.boolean,
                "email": response.response,
                "password": response.status
            }
            print(response)
            return jsonify(reason)
    except Exception as e:
        result = (
                f"-Error "
                + f"{type(e).__name__} {str(e)}"
            )
        print(result)
        return result

@auth_api.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        with grpc.insecure_channel('0.0.0.0:50052') as channel:
            stub = auth_pb2_grpc.LoginServiceStub(channel)
            response = stub.login(auth_pb2.LoginRequest(email=data["email"], password=data["password"]))
            reason = {
                "bool": response.boolean,
                "token": response.response,
                "status": response.status
            }
            print(response)
            return jsonify(reason)
    except Exception as e:
        result = (
                f"-Error "
                + f"{type(e).__name__} {str(e)}"
            )
        print(result)
        return result

