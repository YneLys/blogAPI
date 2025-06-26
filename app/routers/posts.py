from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
from .. import schemas, crud, dependencies, models

router = APIRouter(prefix="/posts", tags=["posts"])

@router.post("/", response_model=schemas.PostOut, status_code=status.HTTP_201_CREATED)
def create_post(post: schemas.PostCreate, db: Session = Depends(dependencies.get_db), current_user: models.User = Depends(dependencies.get_current_user)):
    return crud.create_post(db, post, current_user.id)

@router.get("/", response_model=List[schemas.PostOut])
def list_posts(skip: int = 0, limit: int = 10, db: Session = Depends(dependencies.get_db)):
    posts = crud.get_posts(db, skip=skip, limit=limit)
    return posts

@router.get("/{post_id}", response_model=schemas.PostOut)
def get_post(post_id: int, db: Session = Depends(dependencies.get_db)):
    post = crud.get_post(db, post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@router.put("/{post_id}", response_model=schemas.PostOut)
def update_post(post_id: int, post_update: schemas.PostUpdate, db: Session = Depends(dependencies.get_db), current_user: models.User = Depends(dependencies.get_current_user)):
    db_post = crud.get_post(db, post_id)
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    if db_post.author_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to update this post")
    updated = crud.update_post(db, db_post, post_update)
    return updated

@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int, db: Session = Depends(dependencies.get_db), current_user: models.User = Depends(dependencies.get_current_user)):
    db_post = crud.get_post(db, post_id)
    if not db_post:
        raise HTTPException(status_code=404, detail="Post not found")
    if db_post.author_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this post")
    crud.delete_post(db, db_post)
    return None
