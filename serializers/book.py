from pydantic import BaseModel


class BookSerializer(BaseModel):
    title: str
    author: str