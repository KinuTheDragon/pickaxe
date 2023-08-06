import jwt
import datetime
import os

is_dev_version = "REPL_ID" in os.environ

if not is_dev_version:
    from dotenv import load_dotenv
    load_dotenv()

SECRET_KEY = os.environ["jwt_secret"]

def create_jwt_token(data):
    payload = {
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1),
        "iat": datetime.datetime.utcnow(),
        "data": data
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    return token

def verify_jwt_token(token):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return payload["data"]
    except jwt.ExpiredSignatureError:
        # Token has expired
        return None
    except jwt.InvalidTokenError:
        # Invalid token
        return None