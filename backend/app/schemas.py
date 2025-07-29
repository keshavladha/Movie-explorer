from pydantic import BaseModel
from typing import List, Optional

# Base schemas
class GenreBase(BaseModel):
    name: str
    description: Optional[str] = None

class GenreCreate(GenreBase):
    pass

class Genre(GenreBase):
    id: int
    
    class Config:
        from_attributes = True

# Actor schemas
class ActorBase(BaseModel):
    name: str
    birth_year: Optional[int] = None
    bio: Optional[str] = None

class ActorCreate(ActorBase):
    pass

class Actor(ActorBase):
    id: int
    
    class Config:
        from_attributes = True

class ActorWithMovies(Actor):
    movies: List["MovieSummary"] = []

# Director schemas  
class DirectorBase(BaseModel):
    name: str
    birth_year: Optional[int] = None
    bio: Optional[str] = None

class DirectorCreate(DirectorBase):
    pass

class Director(DirectorBase):
    id: int
    
    class Config:
        from_attributes = True

class DirectorWithMovies(Director):
    movies: List["MovieSummary"] = []

# Movie schemas
class MovieBase(BaseModel):
    title: str
    release_year: int
    synopsis: Optional[str] = None
    duration: Optional[int] = None

class MovieCreate(MovieBase):
    director_id: int
    actor_ids: List[int] = []
    genre_ids: List[int] = []

class MovieSummary(MovieBase):
    id: int
    director: Optional[Director] = None
    
    class Config:
        from_attributes = True

class Movie(MovieBase):
    id: int
    director: Optional[Director] = None
    actors: List[Actor] = []
    genres: List[Genre] = []
    
    class Config:
        from_attributes = True

# Update forward references
ActorWithMovies.model_rebuild()
DirectorWithMovies.model_rebuild() 