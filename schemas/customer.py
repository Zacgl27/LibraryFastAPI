from pydantic import BaseModel
from typing import Optional

class Customer(BaseModel):
    
    customer_id : Optional[int] = None
    customer_name : str = None
    customer_last_name : str = None
    customer_email : str = None
    customer_password : str = None
    customer_address : str = None

    class Config:
        schema_extra = {
            "example": {
                "customer_id" : 123456789,
                "customer_name" : "John",
                "customer_last_name" : "Doe",
                "customer_email" : "john.doe@example.com",
                "cutomer_password" : "password123",
                "customer_address" : "123 Main St, Anytown, USA"
            }
        }