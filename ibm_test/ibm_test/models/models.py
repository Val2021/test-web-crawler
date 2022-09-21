import os
import sys

cwd = os.getcwd()
cwd = cwd.replace("/spiders", "")
sys.path.append(cwd)
from adapters.db import Base
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Boolean, Integer, Text

metadata = Base.metadata


class URL(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True)
    url = Column(Text(500))
    depth = Column(Integer)
    visited = Column(Boolean)

    def __repr__(self) -> str:
        return f"[{self.id},{self.url},{self.depth},{self.visited}]"
