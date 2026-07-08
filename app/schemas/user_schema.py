
from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class User(BaseModel):
    id: int
    name: str 
    email: str  = EmailStr
    age: int


#HomeWork

class UserRegistration(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    email: str = EmailStr
    password: str = Field(
        min_length=8,
        max_length=20,
        description="Password"
    )
    confirm_password: str = Field(
        min_length=8,
        max_length=20,
        description="Confirm Password"
    )

class UserRegistrationResponse(BaseModel):
    message: str
    username: str
    email: str
