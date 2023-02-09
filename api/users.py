from typing import Optional, List
import fastapi
from pydantic import BaseModel


class User(BaseModel):
    name: str
    email: str
    bio: Optional[str]
    is_active: bool


router = fastapi.APIRouter()

users = []


@router.get("/users", response_model=List[User])
async def get_users():
    return users


@router.post("/users")
async def create_user(user: User):
    users.append(user)
    return {"message": "User created successfully"}


# create a get request to get a single user by id
@router.get("/users/{user_id}", response_model=User)
async def get_user(user_id: int):
    return {"user_id": user_id}
