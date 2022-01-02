from pydantic import BaseModel

class User(BaseModel):
    id: str
    first_name: str
    last_name: str 
    email: str
    password: str
    img_url: str
    dark_mode: bool = False
