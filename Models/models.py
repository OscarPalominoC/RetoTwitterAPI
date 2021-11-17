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

# Password mixin
class PasswordMixin(BaseModel):
    Password: str = Field(
        ...,
        min_length=8,
        example="P@ssw0rd!"
    )

# UserBase model
class UserBase(BaseModel):
    UserId: UUID = Field(...)
    Email: EmailStr = Field(..., example="jose@garcia.com")
    
# User login
class UserLogin(UserBase, PasswordMixin):
    pass

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

# User registration
class UserRegister(User, PasswordMixin):
    pass

# Twitter model
class Tweet(BaseModel):
    TweetId: UUID = Field(...)
    Content: str = Field(
        ...,
        min_length=1,
        max_length=250,
        example="Lorem ipsum dolor sit, amet consectetur adipisicing elit. Officiis, ducimus doloribus. Molestiae ad tempore consequuntur maxime aliquid nostrum facilis deleniti laborum assumenda. Doloribus laudantium perspiciatis nemo ex molestias excepturi sit?"
    )
    CreatedAt: datetime = Field(default=datetime.now())
    UpdatedAt: Optional[datetime] = Field(default=None)
    By: User = Field(...)