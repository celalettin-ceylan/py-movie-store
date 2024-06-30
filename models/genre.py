from peewee import CharField
from .base_model import BaseModel
from db import db

class Genre(BaseModel):
    name = CharField(unique=True)

    class Meta:
        table_name = 'genre'