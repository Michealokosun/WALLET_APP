from functools import wraps
from flask import request, jsonify
from api.views.utils.jwt_token import decode_jwt_token

def token_required(f):
    wraps(f)
    def decorated(*arg, **kwargs):
        token = request.headers.get("Authorization")
        if token:
            token = token.split()[1]
        print(token)
        if not token:
            return jsonify({"error": "Token is missing"}), 401
        try:
            payload = decode_jwt_token(token)
            if not payload['sub']:
                return jsonify({"error": "Invalid token"}), 401
        except Exception as e:
            print(e)
            return jsonify({"error": "Invalid token"}), 401
        return f(*arg, **kwargs)
    decorated.__name__ = f.__name__
    return decorated