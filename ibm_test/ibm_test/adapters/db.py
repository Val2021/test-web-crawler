import sqlalchemy as _sql
from sqlalchemy.ext.declarative import declarative_base


DATABASE_URL = "postgresql+psycopg2://ibmpostgres:ibm2022@postgres:5432/ibmdb"

Base = declarative_base()

metadata = Base.metadata
