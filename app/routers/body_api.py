# What is a Request Body?

# A request body is the JSON data sent by the client to the server.

# For example, when creating a new user:
# POST /users
# Body:
# {
#     "name": "Abhishek Kumar",
#     "email": "abhishek@gmail.com",
#     "age": 25
# }
# FastAPI uses Pydantic to validate this data automatically.

from fastapi import APIRouter
from app.schemas.user_schema import User
from app.schemas.user_schema import UserRegistration,UserRegistrationResponse


router = APIRouter(
    prefix="/body",
    tags=["Request Body"]
)


@router.post("/users")
async def create_user(user: User):
    return {
        "message": "User created successfully",
        "data": user
    }

@router.post("/users", response_model=User)
async def create_user(user: User):
    return user


#HomeWork

# Create a Registration API.

# Request
# POST /body/register
# {
#   "username": "abhishek",
#   "email": "abhishek@gmail.com",
#   "password": "Password@123",
#   "confirm_password": "Password@123"
# }
# Response
# {
#   "message": "Registration successful",
#   "username": "abhishek",
#   "email": "abhishek@gmail.com"
# }


@router.post("/register", response_model=UserRegistrationResponse)
async def register_user(user: UserRegistration):
    if user.password != user.confirm_password:
        return {
            "message": "Passwords do not match",
            "username": user.username,
            "email": user.email
        }
    return UserRegistrationResponse(
        message="Registration successful",
        username=user.username,
        email=user.email
    )
