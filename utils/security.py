import os
from dotenv import load_dotenv
import bcrypt
import jwt
from models.validate import Token_Payload

load_dotenv(override=True)

def hash_password(password):
    bytes_pw = str.encode(password)
    return bcrypt.hashpw(bytes_pw, bcrypt.gensalt())

def check_password(password, password_hash):
    bytes_pw = str.encode(password)
    if not bcrypt.checkpw(bytes_pw, password_hash):
        return False
    return True

def generate_token(payload: Token_Payload):
    payload = dict(payload)
    token = jwt.encode(payload, os.environ["SECRET"], algorithm=os.environ["ALGORITHM"])
    return token
