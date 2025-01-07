from dotenv import load_dotenv
from fastapi import FastAPI

from app.routes import router

# Load environment variables from .env file
load_dotenv()
app = FastAPI()

app.include_router(router)
