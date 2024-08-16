from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class sanction(BaseModel):
    
    customer_id: Optional[int] = None
    reason: str =  None
    sanction_date: Optional[datetime] = None

    class Config:
        schema_extra = {
            "example": {
                "customer_id" : "123774",
                "reason" : "puto",
                "sanction_date" : " ",
            }
        }