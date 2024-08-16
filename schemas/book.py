from pydantic import BaseModel, Field
from typing import Optional, List

class Book(BaseModel):

    book_id : Optional[int] = None
    book_name : str = None
    book_category : str = None
    author : str = None

    class Config:
        schema_extra = {
            "example": {
                "book_id" : 1234,
                "book_name" : "John Constantine",
                "book_category" : "Fantasy",
                "author" : "DC",
            }
        }