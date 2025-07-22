from sqlalchemy.orm import Session
from models import models
from fastapi import status
from fastapi.responses import Response

def create(db: Session, sandwich):
    db_item = models.Sandwich(
        name=sandwich.name,
        price=sandwich.price,
        description=sandwich.description
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def read_all(db: Session):
    return db.query(models.Sandwich).all()

def read_one(db: Session, item_id: int):
    return db.query(models.Sandwich).filter(models.Sandwich.id == item_id).first()

def update(db: Session, item_id: int, sandwich):
    db_item = db.query(models.Sandwich).filter(models.Sandwich.id == item_id)
    db_item.update(sandwich.dict(exclude_unset=True), synchronize_session=False)
    db.commit()
    return db_item.first()

def delete(db: Session, item_id: int):
    db_item = db.query(models.Sandwich).filter(models.Sandwich.id == item_id)
    db_item.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)