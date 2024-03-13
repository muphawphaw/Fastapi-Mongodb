from fastapi import APIRouter, Depends , HTTPException
from models.user import User
from config.user_db import get_database
from pymongo import MongoClient
from typing import List
router = APIRouter()

# Route to create a user
@router.post("/users/", response_model=User)
def create_user(create_user: User,db: MongoClient = Depends(get_database)):
    user_dict = create_user.dict(exclude_unset=False)
    
    result = db.users.insert_one(user_dict)
       if not result.acknowledged:
        raise HTTPException
    
    return create_user
 

#route to get all users
@router.get("/users/", response_model=List[User])
def read_all_users(db: MongoClient = Depends(get_database)):
    users_cursor = db.users.find()
    users_list = [User(**user) for user in users_cursor]
    return users_list


