from peewee import CharField, IntegerField, ManyToManyField
from .base_model import BaseModel
from models.movie_type import MovieType
from db import db

class Movie(BaseModel):
    title = CharField()
    year = IntegerField()
    type = types = ManyToManyField(MovieType, backref='movies')