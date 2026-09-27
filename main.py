from fastapi import FastAPI

from config.database import engine
from models.base import BaseModel
from models.book import BookModel
from models.review import ReviewModel

from controllers.review import router as ReviewRouter


BaseModel.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(ReviewRouter)
@app.get('/')
def home():
    return {'message': 'Home Page'}