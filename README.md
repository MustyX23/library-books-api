# Library Books API

A small REST API for keeping track of the books in a library and who has borrowed them.

## Who is it for?

Librarians of **small libraries**, such as a school, a community reading room (читалище) or an office library, and the **readers** who use them.

## What problem does it solve?

Small libraries often track their books and loans on paper or in an Excel sheet. That makes it hard to answer simple questions:

- *Do we have this book?* → search the catalog by title or author
- *Is it on the shelf right now?* → every book shows whether it is borrowed
- *Who has it?* → the borrower's name is stored with the book

Library Books API gives the librarian one place to manage the catalog and the loans, and any app (web page, mobile app, Excel/Power Query) can use it over HTTP.

## Features

| Method | Endpoint | What it does | Ticket |
|--------|----------|--------------|--------|
| `POST` | `/books` | Add a new book | KAN-6 |
| `GET` | `/books` | List all books | KAN-7 |
| `GET` | `/books?q=orwell` | Search by title or author | KAN-11 |
| `GET` | `/books/{id}` | View one book | KAN-8 |
| `PUT` | `/books/{id}` | Edit a book | KAN-9 |
| `DELETE` | `/books/{id}` | Remove a book | KAN-10 |
| `POST` | `/books/{id}/borrow` | Mark a book as borrowed | KAN-2 |
| `POST` | `/books/{id}/return` | Mark a book as returned | KAN-12 |
| `GET` | `/health` | Health check | KAN-1 |

## Running locally

Requires Python 3.12+ (developed on 3.14).

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # macOS / Linux
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000/docs for the interactive Swagger UI.

## Example

```bash
curl -X POST http://127.0.0.1:8000/books -H "Content-Type: application/json" \
     -d '{"title": "1984", "author": "George Orwell", "year": 1949}'

curl -X POST http://127.0.0.1:8000/books/1/borrow -H "Content-Type: application/json" \
     -d '{"borrower": "Ivan"}'
```

## Web UI

A very simple web page lives in `web/` (React + Vite + TypeScript).
Start the API first, then:

```bash
cd web
npm install
npm run dev
```

Open http://localhost:5173. The API address can be changed with `VITE_API_URL`.

## Tests

```bash
pytest
```

Tests also run automatically on every Pull Request via GitHub Actions (KAN-14).

## Project structure

```
app/
  main.py      # FastAPI app and endpoints
  models.py    # Pydantic models
  storage.py   # in-memory storage
tests/         # pytest tests
```

Data is kept in memory to keep the project simple, so it resets on restart.

## Process

Work is planned in Jira (project **KAN**). Every ticket gets its own branch named after its key (e.g. `KAN-6-add-book`). Changes reach `main` only through Pull Requests with the ticket key in the title.
