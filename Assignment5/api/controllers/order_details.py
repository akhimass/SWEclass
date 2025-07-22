from sqlalchemy.orm import Session
from models import models
from fastapi import status
from fastapi.responses import Response

def create(db: Session, detail):
    db_item = models.OrderDetail(
        order_id=detail.order_id,
        sandwich_id=detail.sandwich_id,
        quantity=detail.quantity
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def read_all(db: Session):
    return db.query(models.OrderDetail).all()

def read_one(db: Session, item_id: int):
    return db.query(models.OrderDetail).filter(models.OrderDetail.id == item_id).first()

def update(db: Session, item_id: int, detail):
    db_item = db.query(models.OrderDetail).filter(models.OrderDetail.id == item_id)
    db_item.update(detail.dict(exclude_unset=True), synchronize_session=False)
    db.commit()
    return db_item.first()

def delete(db: Session, item_id: int):
    db_item = db.query(models.OrderDetail).filter(models.OrderDetail.id == item_id)
    db_item.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)