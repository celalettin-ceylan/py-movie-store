import logging
from typing import List
from fastapi import APIRouter, HTTPException
from psycopg2 import IntegrityError
from pydantic import BaseModel
from uuid import UUID
from repositories.movie_repositories import MovieRepository

router = APIRouter()

class MovieItemIn(BaseModel):
    name : str
    year : int
    genres : List[str]

@router.get("/api/movies")
async def get_all_movies():
    try:
        movies = MovieRepository.get_all()
    except IntegrityError as e:
        logging.error(f"Error creating Movie: {e}")
        return HTTPException(status_code=203)
    return movies

@router.get("/api/movie/{uuid}")
async def get_movie(uuid):
    try:
        movie = MovieRepository.get_by_id(uuid)
    except IntegrityError as e:
        logging.error("Error creating Movie: {e}")
        return HTTPException(status_code=203)
    return movie

@router.post("/api/movie")
async def create_movie(items : MovieItemIn):
    try:
        create_movie = MovieRepository.create(name=items.name, year=int(items.year), genres=items.genres)
        return create_movie
    except IntegrityError as e:
        logging.error(f"Error creating Movie: {e}")
    return HTTPException(status_code=203)