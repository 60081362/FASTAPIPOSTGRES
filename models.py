import datetime as _dt
import sqlalchemy as _sql
import database as _database
from database import Base
from sqlalchemy import Boolean,String,Column,Integer,Text


class Item(_database.Base):
    __tablename__='items'
    id=_sql.Column(Integer,primary_key=True, index=True)
    name=_sql.Column(String(255),nullable=False,unique=True)
    surname=_sql.Column(String(255),nullable=False,unique=True)
    age=_sql.Column(Integer,nullable=False)
    description=_sql.Column(String(255),default=False)


    def __repr__(self):
        return f"<Item name={self.name}  age={self.age}>"