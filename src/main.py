import sys, os
sys.path.append(os.path.abspath(os.path.join("..", "fastAPI_practice/routes")))
from fastapi import FastAPI
from routes.users import users
from routes.validate import validate 
from utils.security import hash_password, check_password

app = FastAPI()
app.include_router(users)
app.include_router(validate)


@app.get("/")
def home_route():
    print(">>> waddup!")
    return {
        "route": "home",
        "greeting": "waddup"
    }

@app.post("/")
def hash_check(password: str):
    return { "passwordHash": hash_password(password)}