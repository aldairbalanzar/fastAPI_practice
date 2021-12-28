import sys, os
print("*** " + os.path.abspath(os.path.join("..", "fastAPI_practice/routes")))
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
    


# @app.get("/items/{item_id}")
# def query_route(item_id: int, q: Optional[str]=None):
#     return {
#         "route": "query",
#         "item_id": item_id,
#         "detail": q
#     }