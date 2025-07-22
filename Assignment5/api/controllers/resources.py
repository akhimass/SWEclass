from sqlalchemy.orm import Session
from models import models
from fastapi import status
from fastapi.responses import Response

def create(db: Session, resource):
    db_item = models.Resource(
        name=resource.name,
        quantity=resource.quantity
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def read_all(db: Session):
    return db.query(models.Resource).all()

def read_one(db: Session, item_id: int):
    return db.query(models.Resource).filter(models.Resource.id == item_id).first()

def update(db: Session, item_id: int, resource):
    db_item = db.query(models.Resource).filter(models.Resource.id == item_id)
    db_item.update(resource.dict(exclude_unset=True), synchronize_session=False)
    db.commit()
    return db_item.first()

def delete(db: Session, item_id: int):
    db_item = db.query(models.Resource).filter(models.Resource.id == item_id)
    db_item.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)