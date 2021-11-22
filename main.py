# Python
from typing import List, Optional
import json
from datetime import datetime

# FastAPI
from fastapi import FastAPI
from fastapi import status
from fastapi import Body, Form
from fastapi.exceptions import HTTPException
from pydantic.fields import Field
from pydantic.networks import EmailStr

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
def login(
    email: EmailStr = Form(...), 
    password: str = Form(...)):
    """
    # Login

    This function allows the login to the users.

    ## Parameters
    * email: EmailStr.
    * password: str.

    ## Exceptions
    * HTTPException: If the Email and Password does not match, it raises the message "Incorrect Email/Password!".

    ## Return
    Returns a Json with an  user's basic information
    * UserId: UUID
    * Email: EmailStr
    * FirstName: str
    * LastName: str
    * BirthDate: Optional[date]
    """
    with open("users.json", "r", encoding="utf-8") as f:
        results = json.loads(f.read())
        try:
            for user in results:
                if email == user["Email"] and password == user["Password"]:
                    return user
        except:
            raise HTTPException("Incorrect Email/Password!")

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
    Returns a Json list with all users in the app, with the following keys.
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
def show_an_user(UserId: str):
    """
    # Show an user

    Show an user using the UserId as a parameter.

    # Parameters
    * Request Body Parameter
        * UserId (str)

    ## Returns:
    Returns a Json with an User's Basic Information
    * UserId: UUID
    * Email: EmailStr
    * FirstName: str
    * LastName: str
    * BirthDate: Optional[date]
    """
    with open("users.json", "r", encoding="utf-8") as f:
        results = json.loads(f.read())
        try:
            for user in results:
                if user["UserId"] == UserId:
                    return user
        except:
            raise KeyError("Sorry, that UserId does not exist!")

### Delete an user
@app.delete(
    path="/users/{UserId}/delete",
    status_code=status.HTTP_202_ACCEPTED,
    tags=["Users"],
    summary="Delete an user.",
    response_model=List[User]
    )
def delete_an_user(UserId: str):
    """
    # Delete an user
    
    This function receives an Id and delete the user that owns that Id.

    ## Parameters
    * UserId (str).

    ## Raises:
    * KeyError: If the id doesn't match with any in the results, it raises the KeyError with the message "That user does not exists.".

    ## Returns:
     * List(User)
    """
    with open("users.json", "r+", encoding="utf-8") as f:
        results = json.loads(f.read())
        for user in results:
            if user["UserId"] == UserId:
                f.seek(0)
                results.remove(user)
                f.write(json.dumps(results))
                f.truncate()
        with open("users.json", "r", encoding="utf-8") as f:
            results = json.loads(f.read())
            return results

### Udate an user
@app.put(
    path="/users/{UserId}/update",
    status_code=status.HTTP_200_OK,
    tags=["Users"],
    summary="Update an user.",
    response_model=User
    )
def update_an_user(
    UserId: str,
    Email: EmailStr = Form(...),
    Password: str = Form(...),
    FirstName: str = Form(...),
    LastName: str = Form(...),
    BirthDate: str = Form(...)
    ):
    """
    # Update an user

    Update an user in the app.
    
    ## Parameters
    * UserId (str)
    * Email (EmailStr)
    * Password (str).
    * FirstName (str).
    * LastName (str).
    * Birthdate (Optional[date]).

    ## Returns:
    Returns a Json with an User's Basic Information
    * UserId: UUID
    * Email: EmailStr
    * FirstName: str
    * LastName: str
    * BirthDate: Optional[date]
    """
    with open("users.json", "r+", encoding="utf-8") as f:
        results = json.loads(f.read())
        for i in range(len(results)):
            if results[i]["UserId"] == UserId:
                results[i]["Email"] = Email
                results[i]["Password"] = Password
                results[i]["FirstName"] = FirstName
                results[i]["LastName"] = LastName
                results[i]["BirthDate"] = datetime.strptime(BirthDate, '%d/%m/%Y').date()
                f.seek(0)
                f.write(json.dumps(results, indent=4, default=str))
                f.truncate()
                return results[i]
        return None

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
    # Show all tweets

    This Path Operation shows all tweets in the app.

    ## Parameters
    *No parameters*.

    ## Returns
    Returns a Json list with all tweets in the app, with the following keys.
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
    with open("tweets.json", "r", encoding="utf-8") as f:
        results = json.loads(f.read())
        return results

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
def show_a_tweet(TweetId: str):
    """
    # Show a Tweet

    Show a tweet using the TweetId as a parameter.

    # Parameters
    * Request Body Parameter
        * TweetId (str)

    Returns:
    Returns a Json with a Tweet's Basic Information
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
    with open("tweets.json", "r", encoding="utf-8") as f:
        results = json.loads(f.read())
        try:
            for tweet in results:
                if tweet["TweetId"] == TweetId:
                    return tweet
        except:
            raise KeyError("Sorry, that TweetId does not exist!")

### Delete a tweet
@app.delete(
    path="/tweet/{TweetId}/delete",
    status_code=status.HTTP_202_ACCEPTED,
    tags=["Tweets"],
    summary="Delete a tweet.",
    response_model=List[Tweet]
    )
def delete_a_tweet(TweetId: str):
    """
    # Delete a Tweet
    
    This function receives an Id and delete the tweet that owns that Id.

    ## Parameters
    * TweetId (str).

    ## Returns:
     * List(Tweet)
    """
    with open("tweets.json", "r+", encoding="utf-8") as f:
        results = json.loads(f.read())
        for tweet in results:
            if tweet["TweetId"] == TweetId:
                f.seek(0)
                results.remove(tweet)
                f.write(json.dumps(results))
                f.truncate()
        with open("tweets.json", "r", encoding="utf-8") as f:
            results = json.loads(f.read())
            return results

### Update a tweet
@app.put(
    path="/tweet/{TweetId}/update",
    status_code=status.HTTP_200_OK,
    tags=["Tweets"],
    summary="Update a tweet.",
    response_model=Tweet
    )
def update_a_tweet(
    TweetId: str,
    Content: str = Form(...),
    ):
    """
    # Update a Tweet

    Update a tweet in the app.
    
    ## Parameters
    * TweetId (str)
    * Content (str)

    ## Returns:
    Returns a Json with an tweet's Basic Information
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
        for i in range(len(results)):
            if results[i]["TweetId"] == TweetId:
                results[i]["Content"] = Content
                results[i]["UpdatedAt"] = datetime.now()
                f.seek(0)
                f.write(json.dumps(results, indent=4, default=str))
                f.truncate()
                return results[i]
        return None