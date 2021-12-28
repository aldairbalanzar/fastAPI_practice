from fastapi import APIRouter
from utils.mongo import mongo
from models.user import User
from schemas.user import user_entity, all_users_entity

users = APIRouter()
db = mongo.db

@users.get("/users")
async def find_all_users():
    users_col = db["users"]
    print(">>> getting all users")
    return await all_users_entity(users_col.find())

@users.post("/users")
async def post_user(user: User):
        result = db.insert_one(user)
        print(">>> posting a user")
        return result