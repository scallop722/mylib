from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Boolean
from setting import Base
from setting import ENGINE

class Member(Base):
    """
    Member
    """

    __tablename__ = 'member'
    id = Column(Integer, primary_key=True, autoincrement=True)
    member = relationship("LendingHistory", backref="member")
    name = Column(String(20))
    disabled = Column(Boolean)
    
    def __init__(self, name):
        self.name = name

if __name__ == "__main__":
    Base.metadata.create_all(bind=ENGINE)