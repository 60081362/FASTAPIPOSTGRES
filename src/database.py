import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm
import os


DATABASE_URL =f'postgresql://{os.environ.get("POSTGRES_USER")}:' \
               f'{os.environ.get("POSTGRES_PASSWORD")}@' \
               f'{os.environ.get("POSTGRES_HOST")}:5432/' \
               f'{os.environ.get("POSTGRES_DB")}'

engine=_sql.create_engine(DATABASE_URL,
    echo=True
    )

SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = _declarative.declarative_base()