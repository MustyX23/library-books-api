from fastapi import FastAPI

from app import storage
from app.models import Book, BookIn

app = FastAPI(title="Library Books API")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/books", response_model=Book, status_code=201)
def create_book(data: BookIn):
    return storage.add_book(data)


@app.get("/books", response_model=list[Book])
def list_books():
    return list(storage.books.values())
