import logging
from psycopg2 import IntegrityError
from models.movie import Movie
from models.genre import Genre
class MovieRepository:

    @staticmethod
    def get_all_movies():
        return list(Movie.select())
    
    @staticmethod
    def get_movie_by_id(id):
        return Movie.get_or_none(id = id)
    
    @staticmethod
    def create(name : str, year: int, genres : list):
        try: 
            created_movie = Movie.create(name=name, year=year)
            genres = [Genre.get_by_id(genre) for genre in genres]
            
            logging.info(genres)
            
            created_movie.genres.add(genres)

        except IntegrityError as e:
            logging.error(f"Error creating MovieType: {e}")
            return None
        return created_movie