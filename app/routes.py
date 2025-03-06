from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from app.depends import get_db_session
from app.auth_user import UserUseCases
from app.db.schemas import User
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(prefix="/user")

@router.post("/register")
def user_register(
    user: User,
    db_session: Session = Depends(get_db_session)
):

    uc = UserUseCases(db_session)
    uc.user_register(user=user)

    return JSONResponse(
        content={"msg": "User created"},
        status_code=status.HTTP_201_CREATED
    )


@router.post("/login")
def user_login(
    request_form_user: OAuth2PasswordRequestForm = Depends(),
    db_session: Session = Depends(get_db_session)
):

    uc = UserUseCases(db_session=db_session)
    user = User(
        username = request_form_user.username,
        password = request_form_user.password
    )
    
    auth_data = uc.user_login(user=user)
    
    return JSONResponse(
        content=auth_data,
        status_code=status.HTTP_200_OK
    )

