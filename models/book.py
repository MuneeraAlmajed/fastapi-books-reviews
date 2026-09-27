from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .base import BaseModel

class BookModel(BaseModel):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)

    reviews = relationship("ReviewModel", back_populates="book")