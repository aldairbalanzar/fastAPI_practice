import sys, os
sys.path.append(os.path.abspath(os.path.join("..", "fastAPI_practice/routes")))
from fastapi import FastAPI, HTTPException, Request
from routes.users import users
from routes.validate import validate 
from utils.security import hash_password

app = FastAPI()
app.include_router(users, prefix="/users")
app.include_router(validate, prefix="/validate")


@app.get("/")
def home_route():
    print("\t>>> waddup!")
    return {
        "route": "home",
        "greeting": "waddup"
    }

# @app.post("/")
# def hash_check(password: str):
#     return { "passwordHash": hash_password(password)}