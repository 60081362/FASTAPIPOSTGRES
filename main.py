from typing import TYPE_CHECKING, List
import fastapi as _fastapi
import sqlalchemy.orm as _orm
from fastapi import status,HTTPException
import schemas as _schemas
import services as _services
import uvicorn


if TYPE_CHECKING:
    from sqlalchemy.orm import Session


app=_fastapi.FastAPI()


@app.get('/interns',response_model=List[_schemas.Item],status_code=200)
async def get_all_items(db: _orm.Session = _fastapi.Depends(_services.get_db)):
    return await _services.get_all_items(db=db)


@app.get('/intern/{item_id}',response_model=_schemas.Item)
async def get_an_item(
    item_id: int, db: _orm.Session = _fastapi.Depends(_services.get_db)
):
    item = await _services.get_an_item(db=db, item_id=item_id)
    if item is None:
        raise _fastapi.HTTPException(status_code=404, detail="Contact does not exist")

    return item


@app.post('/intern',response_model=_schemas.Item,
          status_code=status.HTTP_201_CREATED)
async def create_an_item(
    item: _schemas.CreateItem,
    db: _orm.Session = _fastapi.Depends(_services.get_db),
):
    return await _services.create_item(item=item, db=db)


if __name__ == '__main__':
    uvicorn.run("main:app", port=8080, host="0.0.0.0", reload=True)

