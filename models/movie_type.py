from peewee import CharField
from .base_model import BaseModel
from db import db

class MovieType(BaseModel):
    name = CharField(unique=True)