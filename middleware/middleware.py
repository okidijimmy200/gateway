from flask import request, jsonify
from functools import wraps
from provider.auth.auth import Auth

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
            token_request = Auth()
            response = token_request.token(token=token)
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