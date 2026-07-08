# What are GET API ?
# Ans :- GET API is used to retrieve data from the server.
# Syntax :- @router.get("/")



from fastapi import APIRouter

router = APIRouter(
    prefix="/get",
    tags=["GET API"]
)


@router.get("/")
async def home():
    return {
        "message": "Welcome to FastAPI 🚀",
    }


@router.get("/about")
async def about():
    return {
        "name": "Abhishek Kumar",
        "role": "Backend Developer",
        "age": 28,
        "address": {
            "city": "Chapra",
            "state": "Bihar",
            "country": "India",
            "pin-code": "841301"
        },
        "skills": ["Python", "FastAPI", "SQL", "Git", "Docker"]
    }

@router.get("/contact")
async def contact():
    return {
        "email": "abhishek01@gmail.com",
        "phone": "+91-9876543210",
    }