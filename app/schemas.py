
from pydantic import BaseModel, EmailStr, conint
from datetime import datetime
from typing import Optional


#pydantic model (schema)

class UserCreate(BaseModel):
  email: EmailStr
  password: str

class UserOut(BaseModel):
  email: EmailStr
  id: int
  created_at: datetime
  class Config:
    orm_mode = True

class UserLogin(BaseModel):
  email: EmailStr
  password: str

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    

class PostCreate(PostBase):
  pass

class Post(PostBase):
  id: int
  created_at: datetime
  owner_id: int
  owner: UserOut
  #inherited
  # title: str
  # content: str
  # published: bool
  class Config:
    orm_mode = True

class PostOut(BaseModel):
  Post: Post
  votes: int
 

class Token(BaseModel):
  access_token: str
  token_type: str
class TokenData(BaseModel):
  id: str

class Vote(BaseModel):
  post_id: int
  dir: conint(le=1)



