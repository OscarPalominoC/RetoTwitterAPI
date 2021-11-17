# Python
from typing import List
import json

# FastAPI
from fastapi import FastAPI
from fastapi import status
from fastapi import Body

# Models
from Models.models import Tweet, User, UserLogin, UserRegister

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
def signup(user: UserRegister = Body(...)):
    """
# Signup

This Path Operation register an user in the app.

## Parameters:
* Request Body Parameter:
    * user: UserRegister

## Return
Returns a Json with an  user's basic information
* UserId: UUID
* Email: EmailStr
* FirstName: str
* LastName: str
* BirthDate: Optional[date]
    """
    with open("users.json", "r+", encoding="utf-8") as f:
        results = json.loads(f.read())
        user_dict = user.dict()
        user_dict["UserId"] = str(user_dict["UserId"])
        user_dict["BirthDate"] = str(user_dict["BirthDate"])
        results.append(user_dict)
        f.seek(0)
        f.write(json.dumps(results))
        return user


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
    """
# Show all users

This Path Operation shows all users in the app.

## Parameters
*No parameters*.

## Returns
Returns a Json list with all useris in the app, with the following keys.
* UserId: UUID
* Email: EmailStr
* FirstName: str
* LastName: str
* BirthDate: Optional[date]
    """
    with open("users.json", "r", encoding="utf-8") as f:
        results = json.loads(f.read())
        return results

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
def post(tweet: Tweet = Body(...)):
    """
# Post a tweet

This Path Operation post a tweet in the app.

## Parameters:
* Request Body Parameter:
    * tweet: Tweet

## Return
Returns a Json with a Tweet's basic information
* TweetId: UUID
* Content: str
* CreatedAt: datetime
* UpdatedAt: Optional[datetime]
* By: User
    * UserId: UUID
    * Email: EmailStr
    * FirstName: str
    * LastName: str
    * BirthDate: Optional[date]
    """
    with open("tweets.json", "r+", encoding="utf-8") as f:
        results = json.loads(f.read())
        tweet_dict = tweet.dict()
        tweet_dict["TweetId"] = str(tweet_dict["TweetId"])
        tweet_dict["CreatedAt"] = str(tweet_dict["CreatedAt"])
        tweet_dict["UpdatedAt"] = str(tweet_dict["UpdatedAt"])
        tweet_dict["By"]["UserId"] = str(tweet_dict["By"]["UserId"])
        tweet_dict["By"]["BirthDate"] = str(tweet_dict["By"]["BirthDate"])
        
        results.append(tweet_dict)
        f.seek(0)
        f.write(json.dumps(results))
        return tweet

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