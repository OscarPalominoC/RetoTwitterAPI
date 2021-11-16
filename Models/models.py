# Python
from uuid import UUID
from datetime import date, datetime
from typing import Optional

# Pydantic
from pydantic import BaseModel
# Pydantic exotic types
from pydantic import EmailStr
# Pydantic 
from pydantic import Field

# Models

# UserBase model
class UserBase(BaseModel):
    UserId: UUID = Field(...)
    Email: EmailStr = Field(...)
    
# User login
class UserLogin(UserBase):
    Password: str = Field(
        ...,
        min_length=8
    )

# User model
class User(UserBase):
    FirstName: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example="Jose"
    )
    LastName: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example="García"
    )
    BirthDate: Optional[date] = Field(default=None)

# Twitter model
class Tweet(BaseModel):
    TweetId: UUID = Field(...)
    Content: str = Field(
        ...,
        min_length=1,
        max_length=250
    )
    CreatedAt: datetime = Field(default=datetime.now())
    UpdatedAt: Optional[datetime] = Field(default=None)
    By: User = Field(...)