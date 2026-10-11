from pydantic import BaseModel


class BookIn(BaseModel):
    title: str
    author: str
    year: int


class Book(BookIn):
    id: int
