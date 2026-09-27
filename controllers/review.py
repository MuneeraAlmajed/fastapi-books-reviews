from fastapi import APIRouter, HTTPException, Depends

from sqlalchemy.orm import Session

from models.review import ReviewModel

from serializers.review import ReviewSchema, CreateReviewSchema, UpdateReviewSchema

from typing import List

from config.database import get_db


router = APIRouter()

@router.get('/reviews', response_model=List[ReviewSchema])
def get_reviews(db: Session = Depends(get_db)):
    reviews = db.query(ReviewModel).all()
    return reviews

@router.get('/reviews/{review_id}',response_model=ReviewSchema)
def get_single_review(review_id: int, db: Session = Depends(get_db)):
    review = db.query(ReviewModel).filter(ReviewModel.id == review_id).first()
    if not review:
         raise HTTPException(status_code=404, detail="Cannot find review")
    return review
        
@router.post('/reviews', response_model=ReviewSchema)
def create_review(review: CreateReviewSchema, db: Session = Depends(get_db)):
    new_review = ReviewModel(**review.dict())
    
    db.add(new_review)
    db.commit()
    db.refresh(new_review)
    
    return new_review

@router.put('/reviews/{review_id}', response_model=ReviewSchema)
def update_review(review_id: int, review: UpdateReviewSchema, db: Session = Depends(get_db)):
    db_review = db.query(ReviewModel).filter(ReviewModel.id == review_id).first()
    if not db_review:
        raise HTTPException(status_code=404, detail="Cannot find review")
    review_data = review.dict(exclude_unset=True)
    for key, value in review_data.items():
        setattr(db_review, key, value)
    
    db.commit()
    db.refresh(db_review)
    return db_review

@router.delete('/reviews/{review_id}')
def delete_review(review_id: int,db: Session = Depends(get_db)):
    db_review = db.query(ReviewModel).filter(ReviewModel.id == review_id).first()
    if not db_review:
        raise HTTPException(status_code=404, detail="Cannot find review")
    
    db.delete(db_review)
    db.commit()
    return('message:' f'review with ID {review_id} has been deleted')
        

        
