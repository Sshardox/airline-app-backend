from pydantic import BaseModel, constr

class UserBase(BaseModel):
    fullname : constr(min_length=2, max_length=50)
    username : str

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    password: str
    pass

class UserInDBBase(UserBase):
    id: int
    password: str

    model_config = {
        'from_attributes': True
    }

class User(UserBase):
    id: int
    model_config = {
        'from_attributes': True
    }