def test_create_book(client):
    r = client.post("/books", json={"title": "Dune", "author": "Frank Herbert", "year": 1965})
    assert r.status_code == 201
    assert r.json()["id"] == 1
    assert r.json()["title"] == "Dune"


def test_list_books(client, book):
    assert client.get("/books").json() == [book]


def test_list_books_empty(client):
    assert client.get("/books").json() == []


def test_get_book(client, book):
    assert client.get(f"/books/{book['id']}").json() == book


def test_get_missing_book(client):
    assert client.get("/books/999").status_code == 404


def test_update_book(client, book):
    r = client.put(f"/books/{book['id']}", json={"title": "Nineteen Eighty-Four", "author": "George Orwell", "year": 1949})
    assert r.status_code == 200
    assert r.json()["title"] == "Nineteen Eighty-Four"


def test_update_missing_book(client):
    r = client.put("/books/999", json={"title": "X", "author": "Y", "year": 2000})
    assert r.status_code == 404
