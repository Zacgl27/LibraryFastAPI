from pydantic import BaseModel, Field
from typing import Optional, List


class category(BaseModel):
    
    category_id: Optional[int] = None
    category_name: str =  None

    class Config:
        schema_extra = {
            "example": {
                "category_id" : "1245364",
                "category_name" : "puto",
            }
        }