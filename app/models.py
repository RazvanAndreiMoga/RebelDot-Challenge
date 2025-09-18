from sqlalchemy import Column, Integer, String
from pgvector.sqlalchemy import Vector
from .db import Base

class FAQ(Base):
    __tablename__ = "faq"

    id = Column(Integer, primary_key=True, index=True)
    question = Column(String, unique=True, nullable=False)
    answer = Column(String, nullable=False)
    embedding = Column(Vector(1536))
