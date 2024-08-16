from config.database import Base
from sqlalchemy import Column, Integer, String, Float

class Employee(Base):

    __tablename__ = 'employee'

    employee_id = Column(Integer, primary_key=True, nullable=False)
    employee_name = Column(String(50), nullable=False)
    employee_last_name = Column(String(50), nullable=False)
    employee_email = Column(String(70), nullable=False)
    employee_password = Column(String(50), nullable=False)
    job_position = Column(String(50), nullable=False)
    salary = Column(Float, nullable=False)