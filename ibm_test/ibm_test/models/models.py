from xmlrpc.client import Boolean
from sqlalchemy import Column, Integer, String,Boolean
from ibm_test.adapters.db import Base

metadata = Base.metadata

class URL(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String(250))
    depth = Column(Integer)
    visited = Column(Boolean)
    