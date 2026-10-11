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
def list_books(q: str | None = None):
    books = list(storage.books.values())
    if q:
        books = [b for b in books if q in b.title or q in b.author]
    return books


@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    return get_or_404(book_id)


@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, data: BookIn):
    book = get_or_404(book_id)
    updated = book.model_copy(update=data.model_dump())
    storage.books[book_id] = updated
    return updated


@app.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int):
    get_or_404(book_id)
    del storage.books[book_id]
