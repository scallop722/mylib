from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql.sqltypes import Boolean
from setting import Base
from setting import ENGINE

class LendingHistory(Base):
    """
    Book
    """

    __tablename__ = 'book'
    id = Column(Integer, primary_key=True, autoincrement=True)
    lending_date = Column(DateTime)
    returned = Column(Boolean)

    def __init__(self, name):
        self.name = name

if __name__ == "__main__":
    Base.metadata.create_all(bind=ENGINE)