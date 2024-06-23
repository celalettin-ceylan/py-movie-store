import logging
from fastapi import APIRouter, HTTPException
from psycopg2 import IntegrityError
from pydantic import BaseModel
from repositories.movie_type_repository import MovieTypeRepository


router = APIRouter()

class TypeItemIn(BaseModel):
    name: str


class TypeItemOut(TypeItemIn):
    id: int


@router.get("/api/movie-types")
def get_all():
    types = MovieTypeRepository.get_all()
    return types

@router.post("/api/movie-type")
def create(item: TypeItemIn):
    try:
        mtype = MovieTypeRepository.create(item.name)
    except IntegrityError as e:
        logging.error(f"Error creating movie: {e}")
        return HTTPException(status_code=203)
    return mtype