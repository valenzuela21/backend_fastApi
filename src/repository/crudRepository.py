from datetime import datetime
from sqlalchemy.orm import Session
from typing import Type, List
from src.utils.dbUtil import Base


def create_item(db: Session, model: Type[Base], name: str) -> Base:
    db_item = model(name=name)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_item_by_name(db: Session, model: Type[Base], name: str) -> Base:
    return db.query(model).filter(model.name == name).first()

def get_item_by_id(db: Session, model: Type[Base], item_id: int) -> Base:
    return db.query(model).filter(model.id == item_id).first()


def get_all_items(db: Session, model: Type[Base]) -> List[Base]:
    return db.query(model).all()

def update_item(db: Session, model: Type[Base], item_id: int, name: str) -> Base:
    db_item = db.query(model).filter(model.id == item_id).first()
    if db_item:
        db_item.name = name
        db_item.updated_on = datetime.now()
        db.commit()
        db.refresh(db_item)
    return db_item

def delete_item(db: Session, model: Type[Base], item_id: int):
    db_item = db.query(model).filter(model.id == item_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
