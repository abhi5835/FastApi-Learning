from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    name: str
    email: str
    age: int
    # Optional field
    phone: Optional[str] = None
    # Default value field
    is_active: bool = True
    
#HomeWork

class UserRegistration(BaseModel):
    username: str
    email: str
    password: str
    confirm_password: str

class UserRegistrationResponse(BaseModel):
    message: str
    username: str
    email: str
