# Qus :- What are Path Parameters?
# Ans :- Path parameters are dynamic values that are part of the URL.

# Qus :- How to define path parameters?
# Ans :- Path parameters are defined in the URL by enclosing the parameter name in curly braces {}.

# Qus :- How to access path parameters?
# Ans :- Path parameters are accessed in the function parameters by using the same name as the path parameter.
# Example :- @router.get("/users/{user_id}")

# async def get_user(user_id: int):

# Qus :- Why do we use path parameters?
# Ans :- Path parameters are used to define dynamic values that can be used to access specific resources in the API.

# Example :- @router.get("/users/{user_id}")
# async def get_user(user_id: int):

# Type Validation :- 
# FastAPI automatically validates the type of the path parameter.
# Example :- @router.get("/items/{item_id}")

from fastapi import APIRouter

router = APIRouter(
    prefix="/path",
    tags=["Path Parameters"]
)

# Example 1 :- @router.get("/users/{user_id}")
@router.get("/users/{user_id}")
async def get_user(user_id: int):
    return {
        "user_id": user_id,
        "message": f"User {user_id} found."
    }


# Example 2 :- @router.get("/products/{product_id}")
@router.get("/products/{product_id}")
async def get_product(product_id: int):
    return {
        "product_id": product_id,
        "name": f"Product {product_id}"
    }

# Multiple Path Parameters

# Example 1 :-
@router.get("/users/{user_id}/items/{item_id}")
async def get_user_item(user_id: int, item_id: int):
    return {
        "user_id": user_id,
        "item_id": item_id,
        "message": f"User {user_id} found with item {item_id}"
    }

# Example 2 :- @router.get("/stores/{store_id}/products/{product_id}")
@router.get("/stores/{store_id}/products/{product_id}")
async def get_store_product(store_id: int, product_id: int):
    return {
        "store_id": store_id,
        "product_id": product_id,
        "message": f"Store {store_id} found with product {product_id}"
    }

# String Path Parameter
@router.get("/students/{name}")
async def get_student(name: str):
    return {
        "student": name
    }

# Float Path Parameter
@router.get("/price/{amount}")
async def get_price(amount: float):
    return {
        "price": amount
    }

# Boolean Path Parameter
@router.get("/status/{is_active}")
async def get_status(is_active: bool):
    return {
        "is_active": is_active
    }
    

# HomeWork
# Create an endpoint 
# /students/{name}/marks/{marks}
# If marks < 35, return: 
# { 'name': name, 'marks': marks, 'status': 'Fail' }
# If marks >= 35, return: 
# { 'name': name, 'marks': marks, 'status': 'Pass' }
#     

@router.get("/students/{name}/marks/{marks}")
async def get_student_marks(name:str,marks:int):
    if marks < 35:
        return {
            "name": name,
            "marks": marks,
            "status": "Fail"
        }
    else:
        return {
            "name": name,
            "marks": marks,
            "status": "Pass"
        }