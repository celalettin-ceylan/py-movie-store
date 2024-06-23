import logging
import uvicorn
from fastapi import FastAPI
from routers import register
from models import table_utils

def run_app():
    app = FastAPI()
    
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    
    table_utils.create_tables()
    register.register_all_routers(app=app)

    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    run_app()