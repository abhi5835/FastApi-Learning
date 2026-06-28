from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def home():
    return {
        "message": "Welcome to FastAPI 🚀",
    }


@app.get("/about")
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

@app.get("/contact")
async def contact():
    return {
        "email": "abhishek01@gmail.com",
        "phone": "+91-9876543210",
    }

        