from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import crud, models, schemas
from ..database import get_db

router = APIRouter(prefix="/movies", tags=["movies"])

@router.get("/", response_model=List[schemas.MovieSummary])
def read_movies(
    genre_id: Optional[int] = Query(None, description="Filter by genre ID"),
    director_id: Optional[int] = Query(None, description="Filter by director ID"),
    actor_id: Optional[int] = Query(None, description="Filter by actor ID"),
    release_year: Optional[int] = Query(None, description="Filter by release year"),
    db: Session = Depends(get_db)
):
    """Get all movies with optional filtering by genre, director, actor, or release year."""
    movies = crud.get_movies(
        db=db,
        genre_id=genre_id,
        director_id=director_id,
        actor_id=actor_id,
        release_year=release_year
    )
    return movies

@router.get("/{movie_id}", response_model=schemas.Movie)
def read_movie(movie_id: int, db: Session = Depends(get_db)):
    """Get a specific movie by ID with full details including cast and genres."""
    db_movie = crud.get_movie(db, movie_id=movie_id)
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return db_movie

@router.post("/", response_model=schemas.Movie)
def create_movie(movie: schemas.MovieCreate, db: Session = Depends(get_db)):
    """Create a new movie."""
    return crud.create_movie(db=db, movie=movie) 