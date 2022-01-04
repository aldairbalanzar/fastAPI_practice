from pydantic import BaseModel

class User_Validate(BaseModel):
    email: str
    password: str