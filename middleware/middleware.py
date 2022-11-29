import grpc
import generated.auth_pb2 as auth_pb2
import generated.auth_pb2_grpc as auth_pb2_grpc
from flask import request, jsonify
from functools import wraps

'''decorator for verifying jwt'''
def token_required(f):

    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # jwt is passed in the request
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]
            # print(token)
        if not token:
            return {
                "message": "Authentication Token is missing!",
                "data": None,
                "error": "Unauthorized"
            }, 401

        '''decode the payload to get stored details'''
        try:
            # result = get_token.get_current_user_token(f, token, *args, **kwargs)
            with grpc.insecure_channel('0.0.0.0:50052') as channel:
                stub = auth_pb2_grpc.UserManagenmentServiceStub(channel)
                response = stub.ValidateToken(auth_pb2.ValidateTokenRequest(token=token))
                reason = jsonify({
                    "code": response.code,
                    "reason": response.reason,
                    "user_id": response.user_id
                })
                print(reason)
                return f(reason, *args, **kwargs)
        except Exception as e:
            result = (
                    f"-Error "
                    + f"{type(e).__name__} {str(e)}"
                )
            print(result)
            return result

    return decorated