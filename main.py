# Python
from typing import List

# FastAPI
from fastapi import FastAPI
from fastapi import status

# Models
from Models.models import Tweet, User, UserLogin

app = FastAPI()



# Path Operations

## Users

### User registration
@app.post(
    path="/signup",
    status_code=status.HTTP_201_CREATED,
    tags=["Users"],
    summary="User registration.",
    response_model=User
    )
def signup():
    """
# Signup

This Path Operation register an user in the app.

## Parameters:
* Request Body Parameter:
    * user: UserRegister

## Return
Returns a Json with an user's basic information
* UserId: UUID
* Email: EmailStr
* FirstName: str
* LastName: str
* Birthdate: Optional[date]
    """

### User login
@app.post(
    path="/login",
    status_code=status.HTTP_200_OK,
    tags=["Users"],
    summary="User login.",
    response_model=User
    )
def login():
    pass

### Show all users
@app.get(
    path="/users",
    status_code=status.HTTP_200_OK,
    tags=["Users"],
    summary="Show all users.",
    response_model=List[User]
    )
def show_all_users():
    pass

### Show an user
@app.get(
    path="/users/{UserId}",
    status_code=status.HTTP_200_OK,
    tags=["Users"],
    summary="Show a User's details.",
    response_model=User
    )
def show_an_user():
    pass

### Delete an user
@app.delete(
    path="/users/{UserId}/delete",
    status_code=status.HTTP_202_ACCEPTED,
    tags=["Users"],
    summary="Delete an user.",
    response_model=User
    )
def delete_an_user():
    pass

### Udate an user
@app.put(
    path="/users/{UserId}/update",
    status_code=status.HTTP_200_OK,
    tags=["Users"],
    summary="Update an user.",
    response_model=User
    )
def update_an_user():
    pass

## Tweets

### Show all tweets
@app.get(
    path="/",
    status_code=status.HTTP_200_OK,
    tags=["Tweets"],
    summary="Show all the Tweets.",
    response_model=List[Tweet]
    )
def home():
    """
# Home

Show all the tweets.
    """
    return {"API Twitter":"Funcionando"}

### Post a tweet
@app.post(
    path="/post",
    status_code=status.HTTP_201_CREATED,
    tags=["Tweets"],
    summary="Post a tweet.",
    response_model=Tweet
    )
def post():
    pass

### Show a tweet
@app.get(
    path="/tweet/{TweetId}",
    status_code=status.HTTP_200_OK,
    tags=["Tweets"],
    summary="Show a tweet.",
    response_model=Tweet
    )
def show_a_tweet():
    pass

### Delete a tweet
@app.delete(
    path="/tweet/{TweetId}/delete",
    status_code=status.HTTP_202_ACCEPTED,
    tags=["Tweets"],
    summary="Delete a tweet.",
    response_model=Tweet
    )
def delete_a_tweet():
    pass

### Update a tweet
@app.put(
    path="/tweet/{TweetId}/update",
    status_code=status.HTTP_200_OK,
    tags=["Tweets"],
    summary="Update a tweet.",
    response_model=Tweet
    )
def update_a_tweet():
    pass