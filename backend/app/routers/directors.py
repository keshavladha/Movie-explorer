from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from .. import crud, models, schemas
from ..database import get_db

router = APIRouter(prefix="/directors", tags=["directors"])

@router.get("/", response_model=List[schemas.Director])
def read_directors(db: Session = Depends(get_db)):
    """Get all directors."""
    directors = crud.get_directors(db)
    return directors

@router.get("/{director_id}", response_model=schemas.DirectorWithMovies)
def read_director(director_id: int, db: Session = Depends(get_db)):
    """Get a specific director by ID with their filmography."""
    db_director = crud.get_director(db, director_id=director_id)
    if db_director is None:
        raise HTTPException(status_code=404, detail="Director not found")
    return db_director

@router.post("/", response_model=schemas.Director)
def create_director(director: schemas.DirectorCreate, db: Session = Depends(get_db)):
    """Create a new director."""
    return crud.create_director(db=db, director=director) 