from app.models import Book, BookIn

books: dict[int, Book] = {}
_next_id = 1


def add_book(data: BookIn) -> Book:
    global _next_id
    book = Book(id=_next_id, **data.model_dump())
    books[book.id] = book
    _next_id += 1
    return book


def reset() -> None:
    global _next_id
    books.clear()
    _next_id = 1
