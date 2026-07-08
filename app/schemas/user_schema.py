
from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class User(BaseModel):
    name: str = Field(
        min_length=3,
        max_length=50,
        description="User Full Name"
    )
    email: str  = EmailStr
    age: int = Field(
        ge=18,
        le=60,
        description="User Age"
    )
    # Optional field
    phone: Optional[str] = Field(
       min_length=8,
       max_length=20,
       description="User Phone"
    )
    # Default value field
    is_active: bool = True
    
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
