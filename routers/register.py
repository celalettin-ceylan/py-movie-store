from fastapi import FastAPI
from . import movie_router
from . import genre_router

def register_all_routers(app : FastAPI):
    app.include_router(movie_router.router)
    app.include_router(genre_router.router)