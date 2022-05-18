import pydantic as _pydantic


class _BaseItem(_pydantic.BaseModel):
    name:str
    surname:str
    age:int
    description:str

class Item(_BaseItem):
    id: int

    class Config:
        orm_mode=True

class CreateItem(_BaseItem):
    pass