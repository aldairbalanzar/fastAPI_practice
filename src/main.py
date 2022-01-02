import sys, os
sys.path.append(os.path.abspath(os.path.join("..", "fastAPI_practice/routes")))
from fastapi import FastAPI
from routes.users import users

app = FastAPI()
app.include_router(users)

@app.get("/")
def home_route():
    print(">>> waddup!")
    return {
        "route": "home",
        "greeting": "waddup"
    }