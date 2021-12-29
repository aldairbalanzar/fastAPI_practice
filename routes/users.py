from fastapi import APIRouter
from utils.mongo import mongo
from models.user import User
from schemas.user import user_entity, all_users_entity
from bson import ObjectId

users = APIRouter(prefix="/users")
collection = mongo.db["users"]

@users.get("/")
async def find_all_users():
    print("\t>>> getting all users")
    return await all_users_entity(collection.find())

@users.get("/{user_id}")
async def find_user(user_id: str):
    print(f"\t>>> finding user with id: {user_id}")
    found = collection.find_one({"_id": ObjectId(user_id)})
    return user_entity(found)

@users.post("/")
async def post_user(user: User):
        print("\t>>> posting a user")
        collection.insert_one(dict(user))
        return all_users_entity(collection.find())