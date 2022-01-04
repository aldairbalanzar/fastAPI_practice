from fastapi import APIRouter, HTTPException
from utils.mongo import mongo
from utils.security import check_password, generate_token
from models.validate import User_Validate
from schemas.user import user_entity

validate = APIRouter(prefix="/validate")
collection = mongo.db["users"]

@validate.post("/")
async def find_user(data: User_Validate):
    print("\t>>> finding user with provided credentials")
    data = dict(data)
    found = collection.find_one({"email": data["email"]})
    if not found:
        raise HTTPException(status_code=404, detail="User with that email was not found.")
    if not check_password(data["password"], found["password"]):
        raise HTTPException(status_code=404, detail="Password provided is incorrect.")
    print("\t>>> generating token")
    payload ={
        "user_id": found["id"],
        "email": found["email"]
    }
    return generate_token(payload)