from models.movie import Movie

class MovieRepository:

    def get_all_movies():
        return list(Movie.select())
    
    def get_movie_by_id(id):
        return Movie.get_or_none(id = id)