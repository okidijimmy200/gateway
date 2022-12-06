from flask import  request
from flask import Blueprint, jsonify
from provider.auth.auth import Auth

auth_api = Blueprint('auth', __name__)


@auth_api.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        login_client = Auth()
        response = login_client.login(
            email=data["email"], password=data["password"]
        )
        
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



