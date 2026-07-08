#Lesson 3: Query Parameters

#What are Query Parameters?
#Query parameters are values passed after the ? in a URL. They are commonly used for:
#Pagination
#Filtering
#Searching
#Sorting

#Syntax for Query Parameters
#@router.get("/users?page=1")

from fastapi import APIRouter
from typing import Optional

router = APIRouter(
    prefix="/query",
    tags=["Query Parameters"]
)

# Example 1 :- Simple Query Parameters
@router.get("/users")
async def get_users(page: int):
    return {
        "page": page
    }

# Example 2 :- Multiple Query Parameters
@router.get("/products")
async def get_products(category: str, price: float = 0.0):
    return {
        "category": category,
        "price": price
    }

# Example 3 :- Required Query Parameters
@router.get("/items")
async def get_items(item: str,price: float):
    return {
        "item": item,
        "price": price
    }


# Example 4 :- Optional Query Parameters
@router.get("/students")
async def get_students(name: Optional[str] = None):
    return {
        "student": name
    }

# Example 5 :- Default Values
@router.get("/employees")
async def get_employees(page: int = 1, limit: int = 10):
    return {
        "page": page,
        "limit": limit
    }

# Example 6 :- Search API
@router.get("/search")
async def search(query: str):
    return {
        "query": query
    }

# Example 7 :- Filtering 
@router.get("/filter")
async def filter_products(
    category: str,
    min_price: int,
    max_price: int
):
    return {
        "category": category,
        "min_price": min_price,
        "max_price": max_price
    }