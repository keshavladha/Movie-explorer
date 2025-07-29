from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from . import models
import json

def seed_database():
    """Seed the database with sample movie data."""
    db = SessionLocal()
    
    try:
        # Check if data already exists
        if db.query(models.Genre).first():
            print("Database already seeded!")
            return
        
        # Create Genres
        genres_data = [
            {"name": "Action", "description": "High-energy films with intense sequences"},
            {"name": "Drama", "description": "Character-driven narratives exploring human emotions"},
            {"name": "Comedy", "description": "Films designed to entertain and amuse"},
            {"name": "Sci-Fi", "description": "Science fiction and futuristic themes"},
            {"name": "Thriller", "description": "Suspenseful and tension-filled movies"},
            {"name": "Romance", "description": "Love stories and romantic relationships"},
            {"name": "Horror", "description": "Films designed to frighten and create suspense"},
            {"name": "Adventure", "description": "Exciting journeys and quests"},
        ]
        
        genres = []
        for genre_data in genres_data:
            genre = models.Genre(**genre_data)
            db.add(genre)
            genres.append(genre)
        
        db.commit()
        
        # Create Directors
        directors_data = [
            {"name": "Christopher Nolan", "birth_year": 1970, "bio": "British-American film director known for complex narratives and innovative cinematography"},
            {"name": "Quentin Tarantino", "birth_year": 1963, "bio": "American director known for stylized violence and pop culture references"},
            {"name": "Steven Spielberg", "birth_year": 1946, "bio": "American filmmaker and one of the most influential directors in cinema history"},
            {"name": "Martin Scorsese", "birth_year": 1942, "bio": "American director known for crime films and character studies"},
            {"name": "Greta Gerwig", "birth_year": 1983, "bio": "American actress and director known for coming-of-age films"},
        ]
        
        directors = []
        for director_data in directors_data:
            director = models.Director(**director_data)
            db.add(director)
            directors.append(director)
        
        db.commit()
        
        # Create Actors
        actors_data = [
            {"name": "Leonardo DiCaprio", "birth_year": 1974, "bio": "American actor known for intense dramatic performances"},
            {"name": "Margot Robbie", "birth_year": 1990, "bio": "Australian actress known for versatile roles"},
            {"name": "Christian Bale", "birth_year": 1974, "bio": "British actor known for physical transformations"},
            {"name": "Scarlett Johansson", "birth_year": 1984, "bio": "American actress known for action and dramatic roles"},
            {"name": "Ryan Gosling", "birth_year": 1980, "bio": "Canadian actor known for romantic and dramatic roles"},
            {"name": "Emma Stone", "birth_year": 1988, "bio": "American actress known for comedy and musical performances"},
            {"name": "Tom Hardy", "birth_year": 1977, "bio": "British actor known for intense character portrayals"},
            {"name": "Samuel L. Jackson", "birth_year": 1948, "bio": "American actor known for memorable character roles"},
        ]
        
        actors = []
        for actor_data in actors_data:
            actor = models.Actor(**actor_data)
            db.add(actor)
            actors.append(actor)
        
        db.commit()
        
        # Create Movies
        movies_data = [
            {
                "title": "Inception",
                "release_year": 2010,
                "synopsis": "A thief who steals corporate secrets through dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.",
                "duration": 148,
                "director": directors[0],  # Christopher Nolan
                "actors": [actors[0], actors[3]],  # DiCaprio, Johansson
                "genres": [genres[0], genres[3], genres[4]]  # Action, Sci-Fi, Thriller
            },
            {
                "title": "The Dark Knight",
                "release_year": 2008,
                "synopsis": "Batman must face the Joker, a criminal mastermind who wants to plunge Gotham City into anarchy.",
                "duration": 152,
                "director": directors[0],  # Christopher Nolan
                "actors": [actors[2], actors[6]],  # Christian Bale, Tom Hardy
                "genres": [genres[0], genres[1], genres[4]]  # Action, Drama, Thriller
            },
            {
                "title": "Pulp Fiction",
                "release_year": 1994,
                "synopsis": "The lives of two mob hitmen, a boxer, and others intertwine in four tales of violence and redemption.",
                "duration": 154,
                "director": directors[1],  # Quentin Tarantino
                "actors": [actors[7]],  # Samuel L. Jackson
                "genres": [genres[1], genres[4]]  # Drama, Thriller
            },
            {
                "title": "La La Land",
                "release_year": 2016,
                "synopsis": "A jazz musician and an aspiring actress fall in love while pursuing their dreams in Los Angeles.",
                "duration": 128,
                "director": directors[4],  # Greta Gerwig
                "actors": [actors[4], actors[5]],  # Ryan Gosling, Emma Stone
                "genres": [genres[1], genres[5]]  # Drama, Romance
            },
            {
                "title": "The Wolf of Wall Street",
                "release_year": 2013,
                "synopsis": "The story of Jordan Belfort's rise and fall on Wall Street and his life of crime, corruption and federal investigation.",
                "duration": 180,
                "director": directors[3],  # Martin Scorsese
                "actors": [actors[0], actors[1]],  # DiCaprio, Margot Robbie
                "genres": [genres[1], genres[2]]  # Drama, Comedy
            }
        ]
        
        for movie_data in movies_data:
            movie = models.Movie(
                title=movie_data["title"],
                release_year=movie_data["release_year"],
                synopsis=movie_data["synopsis"],
                duration=movie_data["duration"],
                director=movie_data["director"]
            )
            
            # Add relationships
            movie.actors = movie_data["actors"]
            movie.genres = movie_data["genres"]
            
            db.add(movie)
        
        db.commit()
        print("Database seeded successfully!")
        
    except Exception as e:
        print(f"Error seeding database: {e}")
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    seed_database() 