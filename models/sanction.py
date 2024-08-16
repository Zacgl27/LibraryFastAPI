from config.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime 
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

class Sanction(Base):

    __tablename__ = 'sanction'

    customer_id = Column(Integer, ForeignKey('customer.customer_id'), nullable=False)
    reason = Column(String(1000))
    sanction_date = Column(DateTime, default=func.now(), nullable=False)

    customer = relationship("Customer", back_populates="sanction")