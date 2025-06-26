from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, models, dependencies

router = APIRouter(prefix="/users", tags=["users"])

def admin_required(current_user: models.User):
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Admin privileges required")

@router.get("/", response_model=List[schemas.UserOut])
def list_users(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(dependencies.get_db),
    current_user: models.User = Depends(dependencies.get_current_user)
):
    admin_required(current_user)
    return db.query(models.User).offset(skip).limit(limit).all()

@router.get("/{user_id}", response_model=schemas.UserOut)
def get_user_by_id(
    user_id: int,
    db: Session = Depends(dependencies.get_db),
    current_user: models.User = Depends(dependencies.get_current_user)
):
    admin_required(current_user)
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
