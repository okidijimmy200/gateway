from flask import  request
from flask import Blueprint, jsonify
from server.grpc.grpc import AuthClient

registration_api = Blueprint('registration_api', __name__)

'''schema for user model'''

'''signup user'''
@registration_api.route('/signup', methods = ['POST'])
def signup():
    try:
        data = request.get_json()
        signup_client = AuthClient()
        response = signup_client.signup(
            username=data["username"], 
            email=data["email"], 
            password=data["password"]
        )
        
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