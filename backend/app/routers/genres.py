from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import crud, models, schemas
from ..database import get_db

router = APIRouter(prefix="/genres", tags=["genres"])

@router.get("/", response_model=List[schemas.Genre])
def read_genres(db: Session = Depends(get_db)):
    """Get all genres."""
    genres = crud.get_genres(db)
    return genres

@router.get("/{genre_id}", response_model=schemas.Genre)
def read_genre(genre_id: int, db: Session = Depends(get_db)):
    """Get a specific genre by ID."""
    db_genre = crud.get_genre(db, genre_id=genre_id)
    if db_genre is None:
        raise HTTPException(status_code=404, detail="Genre not found")
    return db_genre

@router.post("/", response_model=schemas.Genre)
def create_genre(genre: schemas.GenreCreate, db: Session = Depends(get_db)):
    """Create a new genre."""
    return crud.create_genre(db=db, genre=genre) 