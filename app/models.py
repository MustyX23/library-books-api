from pydantic import BaseModel, Field


class BookIn(BaseModel):
    title: str
    author: str
    year: int


class Book(BookIn):
    id: int
    is_borrowed: bool = False
    borrower: str | None = None


class BorrowRequest(BaseModel):
    borrower: str = Field(min_length=1)
