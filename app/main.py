from app.routers import get_api,path_api,query_api,body_api,curd_api
from fastapi import FastAPI, APIRouter

app = FastAPI()

router = APIRouter()

# GET API with router
app.include_router(get_api.router)

# path parameters with router
app.include_router(path_api.router)

# query parameters with router
app.include_router(query_api.router)

# Request Body with router
app.include_router(body_api.router)

# CRUD APIs with router
app.include_router(curd_api.router)
