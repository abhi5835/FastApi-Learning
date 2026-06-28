from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def Home():
    return {"message": "Hello, I am Start FastApi Learning..."}