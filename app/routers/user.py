from typing import List
from uuid import UUID
from fastapi import APIRouter, status, Depends, Query
from sqlalchemy.orm import Session

from database import get_db_context
from app.services import user as UserService
from services.exception import *
from models import UserViewModel, UserModel

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("", status_code=status.HTTP_200_OK, response_model=List[UserViewModel])
async def get_all_users(
    page: int = Query(ge=1, default=1),
    size: int = Query(ge=1, le=50, default=10),
    db: Session = Depends(get_db_context),
    ):
        return UserService.get_all_users(db)

@router.post("", status_code=status.HTTP_201_CREATED, response_model=UserViewModel)
async def create_book(
    request: UserModel, 
    db: Session = Depends(get_db_context),

    ):  

        return UserService.add_new_user(db, request)

@router.get("/{user_id}", response_model=UserViewModel)
async def get_user_detail(user_id: UUID, db: Session=Depends(get_db_context)):
    user = UserService.get_user_by_id(db, user_id, joined_load=True)
    
    if user is None:
        raise ResourceNotFoundError()

    return user


@router.put("/{user_id}", status_code=status.HTTP_200_OK, response_model=UserViewModel)
async def update_user(
    user_id: UUID,
    request: UserModel,
    db: Session=Depends(get_db_context),
    ):
        return UserService.update_user(db, user_id, request)
