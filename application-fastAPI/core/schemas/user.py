from pydantic import BaseModel


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    pass


class UserRead(UserBase):
    # model_config = ConfigDict(
    #     from_attributes=True
    # )
    id: int
