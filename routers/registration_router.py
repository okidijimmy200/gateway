import grpc
import generated.auth_pb2 as auth_pb2
import generated.auth_pb2_grpc as auth_pb2_grpc
from flask import  request
from flask import Blueprint, jsonify

registration_api = Blueprint('registration_api', __name__)

'''schema for user model'''

'''signup user'''
@registration_api.route('/signup', methods = ['POST'])
def signup():
    try:
        data = request.get_json()
        with grpc.insecure_channel('0.0.0.0:50052') as channel:
            stub = auth_pb2_grpc.UserManagenmentServiceStub(channel)
            response = stub.SignUp(auth_pb2.SignUpRequest(username=data["username"], email=data["email"], password=data["password"]))
            reason = {
                "code": response.code,
                "reason": response.reason
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