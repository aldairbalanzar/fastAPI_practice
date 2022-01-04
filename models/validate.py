from pydantic import BaseModel

class User_Validate(BaseModel):
    email: str
    password: str

class Token_Payload(BaseModel):
    user_id: str
    email: str