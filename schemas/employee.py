from pydantic import BaseModel
from typing import Optional

class Employee(BaseModel):
    
    employee_id : Optional[int] = None
    employee_name : str = None
    employee_last_name : str = None
    employee_email : str = None
    employee_password : str = None
    job_position : str = None
    salary : float = None

    class Config:
        schema_extra = {
            "example": {
                "employee_id": 1,
                "employee_name": "John",
                "employee_last_name": "Doe",
                "employee_email": "john.doe@example.com",
                "employee_password": "password123",
                "job_position": "Software Engineer",
                "salary": 50000.0
            }
        }