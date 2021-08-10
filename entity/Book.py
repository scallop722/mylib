from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from setting import Base
from setting import ENGINE

class Book(Base):
    """
    Book
    """

    __tablename__ = 'book'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(30))
    author = Column(String(30))
    note = Column(String)

    def __init__(self, name):
        self.name = name

if __name__ == "__main__":
    Base.metadata.create_all(bind=ENGINE)