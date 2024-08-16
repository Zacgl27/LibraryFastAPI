from config.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

class Activity_History(Base):

    __tablename__ = 'activity_history'

    customer_id = Column(Integer, ForeignKey('customer.customer.id'), nullable=False)
    book_id = Column(Integer, ForeignKey('book.book_id'), nullable=False)
    activity_type = Column(String, nullable=False)
    activity_date = Column(DateTime, default=func.now(), nullable=False)

    customer = relationship("Customer", back_populates="activity_history")
    book = relationship("Book", back_populates="activity_history")