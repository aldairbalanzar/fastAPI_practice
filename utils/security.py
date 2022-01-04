import bcrypt

def hash_password(password):
    bytes_pw = str.encode(password)
    return bcrypt.hashpw(bytes_pw, bcrypt.gensalt())

def check_password(password, password_hash):
    bytes_pw = str.encode(password)
    if not bcrypt.checkpw(bytes_pw, password_hash):
        return False
    return True