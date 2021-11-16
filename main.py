# Python
from typing import List

# FastAPI
from fastapi import FastAPI
from fastapi import status

# Models
from Models.models import User, UserLogin

app = FastAPI()



# Path Operations
@app.get(
    path="/",
    status_code=status.HTTP_200_OK,
    tags=["Home"],
    summary="Home of the webpage."
    )
def home():
    """
# Home

This is the project's landing page.
    """
    return {"API Twitter":"Funcionando"}

## Users

@app.post(
    path="/signup",
    status_code=status.HTTP_201_CREATED,
    tags=["Users"],
    summary="User registration.",
    response_model=User
    )
def signup():
    pass

@app.post(
    path="/login",
    status_code=status.HTTP_200_OK,
    tags=["Users"],
    summary="User login.",
    response_model=User
    )
def login():
    pass

@app.get(
    path="/users",
    status_code=status.HTTP_200_OK,
    tags=["Users"],
    summary="Show all users.",
    response_model=List[User]
    )
def show_all_users():
    pass

@app.get(
    path="/users/{UserId}",
    status_code=status.HTTP_200_OK,
    tags=["Users"],
    summary="Show a User's details.",
    response_model=User
    )
def show_an_user():
    pass

@app.delete(
    path="/users/{UserId}/delete",
    status_code=status.HTTP_202_ACCEPTED,
    tags=["Users"],
    summary="Delete an user.",
    response_model=User
    )
def delete_an_user():
    pass

@app.put(
    path="/users/{UserId}/update",
    status_code=status.HTTP_200_OK,
    tags=["Users"],
    summary="Update an user.",
    response_model=User
    )
def update_an_user():
    pass
