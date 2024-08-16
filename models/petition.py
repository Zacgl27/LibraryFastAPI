from config.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

class Petition(Base):

    __tablename__ = 'petition'

    petition_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    customer_id = Column(Integer, ForeignKey('customer.customer_id'), nullable=False)
    book_id = Column(Integer, ForeignKey('book.book_id'), nullable=False)
    petition_date = Column(DateTime, default=func.now(), nullable=False)

    customer = relationship("Customer", back_populates="petition")
    book = relationship("Book", back_populates="petition")
    petition_status = relationship("Petition_Status", back_populates="petition")