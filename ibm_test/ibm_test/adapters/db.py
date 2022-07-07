import sqlalchemy as _sql
from sqlalchemy.ext.declarative import declarative_base

# import sqlalchemy.orm as _orm
from sqlalchemy.orm import scoped_session, sessionmaker

DATABASE_URL = "postgresql+psycopg2://ibm-postgres:ibm2022@postgres:5432/postgres"

engine = _sql.create_engine(DATABASE_URL)


Session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))


Base = declarative_base()

metadata = Base.metadata
