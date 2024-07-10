import logging
from fastapi import APIRouter, HTTPException
from psycopg2 import IntegrityError
from pydantic import BaseModel
from repositories.genre_repositories import GenreRepository

router = APIRouter()

class GenreItemIn(BaseModel):
    name: str


class GenreItemOut(GenreItemIn):
    id: int


@router.get("/api/genres")
def get_all():
    types = GenreRepository.get_all()
    return types

@router.post("/api/genre")
def create(item: GenreItemIn):
    try:
        mtype = GenreRepository.create(item.name)
    except IntegrityError as e:
        logging.error(f"Error creating movie: {e}")
        return HTTPException(status_code=203)
    return mtype