from sqlalchemy.orm import Session
from models import models
from fastapi import status
from fastapi.responses import Response

def create(db: Session, recipe):
    db_item = models.Recipe(
        sandwich_id=recipe.sandwich_id,
        resource_id=recipe.resource_id,
        quantity=recipe.quantity
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def read_all(db: Session):
    return db.query(models.Recipe).all()

def read_one(db: Session, item_id: int):
    return db.query(models.Recipe).filter(models.Recipe.id == item_id).first()

def update(db: Session, item_id: int, recipe):
    db_item = db.query(models.Recipe).filter(models.Recipe.id == item_id)
    db_item.update(recipe.dict(exclude_unset=True), synchronize_session=False)
    db.commit()
    return db_item.first()

def delete(db: Session, item_id: int):
    db_item = db.query(models.Recipe).filter(models.Recipe.id == item_id)
    db_item.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)