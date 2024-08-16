from pydantic import BaseModel, Field
from typing import Optional, List

class petition_status(BaseModel):
    
    petition_id: Optional[int] = None 
    petition_status : bool = None

    class Config:
        schema_extra = {
            "example": {
                "petition_id" : 123664,
                "patition_status" : " ",
            }
        }