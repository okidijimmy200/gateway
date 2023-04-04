from flask import jsonify, request
from functools import wraps
from service.interface import TokenProvider


'''decorator for verifying jwt'''
class TokenRequiredService:
    def __init__(self, deco: TokenProvider) -> None:
        self.deco = deco

    '''decorator for verifying jwt'''
    def validate_token(self, f):

        @wraps(f)
        def decorated(*args, **kwargs):
            token = None
            # jwt is passed in the request
            if "Authorization" in request.headers:
                token = request.headers["Authorization"].split(" ")[1]
                
            if not token:
                return {
                    "message": "Authentication Token is missing!",
                    "data": None,
                    "error": "Unauthorized"
                }, 401

            '''decode the payload to get stored details'''
            try:
                # result = get_token.get_current_user_token(f, token, *args, **kwargs)
                response = self.deco.validate_token(token)
                # if type(response.user_id)
                reason = jsonify({
                    "code": response.code,
                    "reason": response.reason,
                    "user_id": response.user_id
                })
                return f(reason, *args, **kwargs)
            except Exception as e:
                result = (
                        f"-Error "
                        + f"{type(e).__name__} {str(e)}"
                    )
                print(result)
                return result

        return decorated




