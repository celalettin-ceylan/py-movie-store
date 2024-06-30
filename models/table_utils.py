from db import db
from models.movie import Movie
from models.genre import Genre

def create_tables():
    db.create_tables([Genre, 
                      Movie, 
                      Movie.genres.get_through_model()])