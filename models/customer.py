from config.database import Base
from sqlalchemy import Column, Integer, String

class Customer(Base):

    __tablename__ = 'customer'

    customer_id = Column(Integer, primary_key=True, nullable=False)
    customer_name = Column(String(50), nullable=False)
    customer_last_name = Column(String(50), nullable=False)
    customer_email = Column(String(70), nullable=False)
    customer_password = Column(String(50), nullable=False)
    customer_address = Column(String(50), nullable=False)
