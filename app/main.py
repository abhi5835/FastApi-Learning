from app.routers import get_api,path_api
from fastapi import FastAPI, APIRouter

app = FastAPI()

router = APIRouter()

# GET API with router
app.include_router(get_api.router)

# path parameters with router
app.include_router(path_api.router)
