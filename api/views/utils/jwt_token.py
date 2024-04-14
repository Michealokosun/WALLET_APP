from datetime import datetime, timedelta
import jwt

my_secrete = "my super secrete"

def create_jwt_token(user_id: int) -> str:
    payload = {
		'exp': datetime.now() + timedelta(days=1),
		'iat': datetime.utcnow(),
		'sub': user_id
	}
    return jwt.encode(
        payload,
        my_secrete,
        algorithm='HS256'
    )
 
def decode_jwt_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, my_secrete, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return {"error": "Token has expired"}
    except jwt.InvalidTokenError:
        return {"error": "Invalid token"}
    except Exception as e:
        return {"error": "An error occurred", "details": str(e)}
