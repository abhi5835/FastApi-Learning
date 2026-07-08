from fastapi import APIRouter
from app.schemas.user_schema import User

router = APIRouter(
    prefix="/users",
    tags=["CRUD APIs"]
)

# In-memory storage for users
users = []

# Create a new user
@router.post("/")
async def create_user(user: User):
    print(user.id)
    user.id = len(users) + 1
    print(user.id)
    users.append(user)
    print(users)
    return {
        "message": "User created successfully",
        "data": user
    }

# GET All Users
@router.get("/")
async def get_all_users():
    return {
        "message": "Users fetched successfully",
        "data": users
    }

# GET User by ID
@router.get("/userss/{user_id}")
async def get_user_by_id(user_id: int):
    for user in users:
        if user.id == user_id:
            return {
                "message": "User fetched successfully",
                "data": user
            }
    return {
        "message": "User not found",
        "data": None
    }

# Update User
@router.put("/{user_id}")
async def update_user(user_id: int, updated_user: User):
    for index, user in enumerate(users):
        if user.id == user_id:
            users[index] = updated_user
            return {
                "message": "User updated successfully",
                "data": updated_user
            }
    return {
        "message": "User not found",
        "data": None
    }

# Delete User
@router.delete("/{user_id}")
async def delete_user(user_id: int):
    for index, user in enumerate(users):
        if user.id == user_id:
            users.pop(index)
            return {
                "message": "User deleted successfully",
                "data": user
            }
    return {
        "message": "User not found",
        "data": None
    }