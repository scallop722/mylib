from typing import List
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from setting import Base
from setting import ENGINE

class Book(Base):
    """
    Book
    """

    __tablename__ = 'book'
    id = Column(Integer, primary_key=True, autoincrement=True)
    lending_histories = relationship("LendingHistory", backref="book")
    title = Column(String(30))
    author = Column(String(30))
    note = Column(String)

    def __init__(self, name):
        self.name = name

    def get_planed_return_date(self):
        if ([history for history in self.lending_histories if not history.returned ]):
            return "貸出中"
        else:
            return "返却済み"


if __name__ == "__main__":
    Base.metadata.create_all(bind=ENGINE)