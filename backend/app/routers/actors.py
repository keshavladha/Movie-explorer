from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import crud, models, schemas
from ..database import get_db

router = APIRouter(prefix="/actors", tags=["actors"])

@router.get("/", response_model=List[schemas.Actor])
def read_actors(
    movie_id: Optional[int] = Query(None, description="Filter by movie ID"),
    genre_id: Optional[int] = Query(None, description="Filter by genre ID (based on movies they've acted in)"),
    db: Session = Depends(get_db)
):
    """Get all actors with optional filtering by movie or genre."""
    actors = crud.get_actors(db=db, movie_id=movie_id, genre_id=genre_id)
    return actors

@router.get("/{actor_id}", response_model=schemas.ActorWithMovies)
def read_actor(actor_id: int, db: Session = Depends(get_db)):
    """Get a specific actor by ID with their movie filmography."""
    db_actor = crud.get_actor(db, actor_id=actor_id)
    if db_actor is None:
        raise HTTPException(status_code=404, detail="Actor not found")
    return db_actor

@router.post("/", response_model=schemas.Actor)
def create_actor(actor: schemas.ActorCreate, db: Session = Depends(get_db)):
    """Create a new actor."""
    return crud.create_actor(db=db, actor=actor) 