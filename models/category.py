from config.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Category(Base):

    __tablename__ = 'category'

    category_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    category_name = Column(String(100), nullable=False)

    book = relationship("Book", back_populates="category")