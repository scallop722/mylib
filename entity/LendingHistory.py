from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Boolean
from setting import Base
from setting import ENGINE

class LendingHistory(Base):
    """
    LendingHistory
    """

    __tablename__ = 'lending_history'
    id = Column(Integer, primary_key=True, autoincrement=True)
    book_id = Column(Integer, ForeignKey('book.id'))
    member_id = Column(Integer, ForeignKey('member.id'))
    lending_date = Column(DateTime)
    returned = Column(Boolean)

    def __init__(self, name):
        self.name = name

if __name__ == "__main__":
    Base.metadata.create_all(bind=ENGINE)