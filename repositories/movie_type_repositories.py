import logging

from psycopg2 import IntegrityError
from models.movie_type import MovieType

class MovieTypeRepository():

    @staticmethod
    def get_all():
        return list(MovieType.select())
    
    @staticmethod
    def get_by_id(id):
        return MovieType.get_by_id(id)
    
    @staticmethod
    def create(mname : str):
        try:
            created_mtype = MovieType.create(name=mname)
            return created_mtype
        except IntegrityError as e:
            logging.error(f"Error creating MovieType: {e}")
        return None