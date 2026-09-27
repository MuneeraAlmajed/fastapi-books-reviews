from pydantic import BaseModel


class ReviewSchema(BaseModel):
    id: int
    content: str
    rating: int
    book_id: int


class CreateReviewSchema(BaseModel):
    content: str
    rating: int
    book_id: int


class UpdateReviewSchema(BaseModel):
    content: str | None = None
    rating: int | None = None
    book_id: int | None = None