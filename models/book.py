from config.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class Book(Base):

    __tablename__ = 'books'

    book_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    book_name = Column(String(50), nullable=False)
    book_category = Column(Integer, ForeignKey('category.category_id'))
    author = Column(String(50), nullable=False)
    
    category = relationship("Category", back_populates="book")
    activity_history = relationship("Activity_History", back_populates="book")
    petition = relationship("Petition", back_populates="book")