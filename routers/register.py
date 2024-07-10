from fastapi import FastAPI
from .api import movie_router
from .api import genre_router

def register_all_routers(app : FastAPI):
    app.include_router(movie_router.router)
    app.include_router(genre_router.router)