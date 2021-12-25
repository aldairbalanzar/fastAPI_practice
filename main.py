from typing import Optional
from fastapi import FastAPI
from pprint import pprint
from mongo import Mongo

mongo = Mongo()
print(mongo.connection_string)
mongo.connect()

app = FastAPI()

# @app.get("/")
# def home_route():
#     return {
#         "route": "home",
#         "greeting": "waddup"
#     }

# @app.get("/items/{item_id}")
# def query_route(item_id: int, q: Optional[str]=None):
#     return {
#         "route": "query",
#         "item_id": item_id,
#         "detail": q
#     }