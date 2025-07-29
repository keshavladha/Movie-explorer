from sqlalchemy.orm import Session
from sqlalchemy import and_, or_
from typing import List, Optional
from . import models, schemas

# Genre CRUD
def get_genres(db: Session) -> List[models.Genre]:
    return db.query(models.Genre).all()

def get_genre(db: Session, genre_id: int) -> Optional[models.Genre]:
    return db.query(models.Genre).filter(models.Genre.id == genre_id).first()

def create_genre(db: Session, genre: schemas.GenreCreate) -> models.Genre:
    db_genre = models.Genre(**genre.dict())
    db.add(db_genre)
    db.commit()
    db.refresh(db_genre)
    return db_genre

# Director CRUD
def get_directors(db: Session) -> List[models.Director]:
    return db.query(models.Director).all()

def get_director(db: Session, director_id: int) -> Optional[models.Director]:
    return db.query(models.Director).filter(models.Director.id == director_id).first()

def create_director(db: Session, director: schemas.DirectorCreate) -> models.Director:
    db_director = models.Director(**director.dict())
    db.add(db_director)
    db.commit()
    db.refresh(db_director)
    return db_director

# Actor CRUD
def get_actors(db: Session, movie_id: Optional[int] = None, genre_id: Optional[int] = None) -> List[models.Actor]:
    query = db.query(models.Actor)
    
    if movie_id:
        query = query.join(models.movie_actors).filter(models.movie_actors.c.movie_id == movie_id)
    
    if genre_id:
        query = query.join(models.movie_actors).join(models.Movie).join(models.movie_genres).filter(
            models.movie_genres.c.genre_id == genre_id
        )
    
    return query.all()

def get_actor(db: Session, actor_id: int) -> Optional[models.Actor]:
    return db.query(models.Actor).filter(models.Actor.id == actor_id).first()

def create_actor(db: Session, actor: schemas.ActorCreate) -> models.Actor:
    db_actor = models.Actor(**actor.dict())
    db.add(db_actor)
    db.commit()
    db.refresh(db_actor)
    return db_actor

# Movie CRUD
def get_movies(
    db: Session, 
    genre_id: Optional[int] = None,
    director_id: Optional[int] = None,
    actor_id: Optional[int] = None,
    release_year: Optional[int] = None
) -> List[models.Movie]:
    query = db.query(models.Movie)
    
    if genre_id:
        query = query.join(models.movie_genres).filter(models.movie_genres.c.genre_id == genre_id)
    
    if director_id:
        query = query.filter(models.Movie.director_id == director_id)
    
    if actor_id:
        query = query.join(models.movie_actors).filter(models.movie_actors.c.actor_id == actor_id)
    
    if release_year:
        query = query.filter(models.Movie.release_year == release_year)
    
    return query.all()

def get_movie(db: Session, movie_id: int) -> Optional[models.Movie]:
    return db.query(models.Movie).filter(models.Movie.id == movie_id).first()

def create_movie(db: Session, movie: schemas.MovieCreate) -> models.Movie:
    # Create movie without relationships first
    movie_data = movie.dict()
    actor_ids = movie_data.pop('actor_ids', [])
    genre_ids = movie_data.pop('genre_ids', [])
    
    db_movie = models.Movie(**movie_data)
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    
    # Add actor relationships
    if actor_ids:
        actors = db.query(models.Actor).filter(models.Actor.id.in_(actor_ids)).all()
        db_movie.actors = actors
    
    # Add genre relationships
    if genre_ids:
        genres = db.query(models.Genre).filter(models.Genre.id.in_(genre_ids)).all()
        db_movie.genres = genres
    
    db.commit()
    db.refresh(db_movie)
    return db_movie 