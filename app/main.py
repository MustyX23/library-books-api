from fastapi import FastAPI, HTTPException

from app import storage
from app.models import Book, BookIn

app = FastAPI(title="Library Books API")


def get_or_404(book_id: int) -> Book:
    book = storage.books.get(book_id)
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/books", response_model=Book, status_code=201)
def create_book(data: BookIn):
    return storage.add_book(data)


@app.get("/books", response_model=list[Book])
def list_books():
    return list(storage.books.values())


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    return get_or_404(book_id)
