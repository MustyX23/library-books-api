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
