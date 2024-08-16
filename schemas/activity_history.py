from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class activity_history(BaseModel):

    customer_id: Optional[int] = None 
    book_id : Optional[int] = None
    activity_type : str = None
    activity_date : Optional[datetime] = None
    
    class Config:
        schema_extra = {
            "example": {
                "customer_id" : 123774,
                "book_id" : "78765",
                "activity_type" : "Loan or repayment",
                "activity_date" : " ",
               
            }
        }