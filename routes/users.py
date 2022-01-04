from fastapi import APIRouter, HTTPException
from utils.mongo import mongo
from utils.security import hash_password
from models.user import User
from schemas.user import user_entity, all_users_entity
from bson import ObjectId

users = APIRouter(prefix="/users")
collection = mongo.db["users"]

@users.get("/")
async def find_all_users():
    print("\t>>> getting all users")
    return all_users_entity(collection.find())

@users.get("/{user_id}")
async def find_user(user_id: str):
    print(f"\t>>> finding user with id: {user_id}")
    found = collection.find_one({"_id": ObjectId(user_id)})
    if not found:
        raise HTTPException(status_code=404, detail=f"User with id {user_id} was not found.")
    return user_entity(found)

@users.post("/")
async def post_user(user: User):
    print("\t>>> posting a user")
    user = dict(user)
    user["password"] = hash_password(user["password"])
    collection.insert_one(user)
    return all_users_entity(collection.find())

@users.put("/{user_id}")
async def put_user(user_id: str, user: User):
    print(f"\t>>> finding user with id: {user_id}")
    found = collection.find_one({"_id": ObjectId(user_id)})
    if not found:
        raise HTTPException(status_code=404, detail=f"User with id {user_id} was not found.")
    print("\t>>> putting a user")
    collection.find_one_and_update({"_id": ObjectId(user_id)}, {"$set": dict(user)})
    return user_entity(collection.find_one({"_id": ObjectId(user_id)}))

@users.delete("/{user_id}")
async def delete_user(user_id: str):
    print(f"\t>>> finding user with id: {user_id}")
    found = collection.find_one({"_id": ObjectId(user_id)})
    if not found:
        raise HTTPException(status_code=404, detail=f"User with id {user_id} was not found.")
    print("\t>>> deleting user")
    collection.find_one_and_delete({"_id": ObjectId(user_id)})
    return all_users_entity(collection.find())