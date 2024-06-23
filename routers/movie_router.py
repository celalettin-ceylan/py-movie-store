from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/movies")
async def get_all_movies():
    return {"movies" : "All Movies"}

@router.get("/movie/{id}")
async def get_movie(id):
    return {"movie" : id + ". movie is getting"}