import logging

from psycopg2 import IntegrityError
from models.genre import Genre

class GenreRepository():

    @staticmethod
    def get_all():
        return list(Genre.select())
    
    @staticmethod
    def get_by_id(id):
        return Genre.get_by_id(id)
    
    @staticmethod
    def create(mname : str):
        try:
            created_mtype = Genre.create(name=mname)
        except IntegrityError as e:
            logging.error(f"Error creating MovieType: {e}")
            return None
        return created_mtype