import sqlalchemy as _sql
import sqlalchemy.orm as _orm
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "postgresql+psycopg2://ibm-postgres:ibm2022@postgres:5432/postgres"

engine = _sql.create_engine(DATABASE_URL)

Session = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()

metadata = Base.metadata


def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()