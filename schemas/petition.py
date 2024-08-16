from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class petition(BaseModel):
    
    petition_id: Optional[int] = None
    customer_id: Optional[int] = None
    book_id: Optional[int] = None 
    petition_status : bool = None
    petition_date: Optional[datetime] = None

    class Config:
        schema_extra = {
            "example": {
                "petition_id" : "9876",
                "customer_id" : "123774",
                "book_id" : "78765",
                "petition_date" : " ",
            }
        }