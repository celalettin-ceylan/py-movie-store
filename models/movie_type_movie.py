from models.base_model import BaseModel
from models.movie import Movie
from models.movie_type import MovieType
from peewee import ForeignKeyField

class MovieTypeAndMovie(BaseModel):
    movie = ForeignKeyField(Movie, backref='types')
    movie_type = ForeignKeyField(MovieType, backref='movies')