import sys

sys.path.append("/home/val/test-web-crawler/ibm_test/ibm_test")
from adapters.db import Base
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Boolean, Integer, String

metadata = Base.metadata


class URL(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(String(250))
    depth = Column(Integer)
    visited = Column(Boolean)

    def __repr__(self) -> str:
        return f"[{self.id},{self.url},{self.depth},{self.visited}]"
