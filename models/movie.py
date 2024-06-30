from peewee import CharField, IntegerField, ManyToManyField
from .base_model import BaseModel
from models.genre import Genre
from db import db

class Movie(BaseModel):
    name = CharField()
    year = IntegerField()
    genres = ManyToManyField(Genre, backref='movies')