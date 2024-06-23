from fastapi import FastAPI
from . import movie_router
from . import movie_type_router

def register_all_routers(app : FastAPI):
    app.include_router(movie_router.router)
    app.include_router(movie_type_router.router)