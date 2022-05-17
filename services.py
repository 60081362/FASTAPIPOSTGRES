from typing import TYPE_CHECKING, List

import database as _database
import models as _models
import schemas as _schemas


if TYPE_CHECKING:
    from sqlalchemy.orm import Session


def _add_tables():
    return _database.Base.metadata.create_all(bind=_database.engine)

def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def create_item(
    item: _schemas.CreateItem, db: "Session"
) -> _schemas.Item:
    item = _models.Item(**item.dict())
    db.add(item)
    db.commit()
    db.refresh(item)
    return _schemas.Item.from_orm(item)

async def get_all_items(db: "Session") -> List[_schemas.Item]:
    items = db.query(_models.Item).all()
    return list(map(_schemas.Item.from_orm, items))


async def get_an_item(item_id: int, db: "Session"):
    item = db.query(_models.Item).filter(_models.Item.id == item_id).first()
    return item