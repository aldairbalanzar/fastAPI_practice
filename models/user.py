from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: str
    first_name: str
    last_name: str 
    email: str
    password: str
    img_url: Optional[str] = ""
    dark_mode: Optional[bool] = False

class User_Update(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str
    img_url: Optional[str]
    dark_mode: Optional[bool]
