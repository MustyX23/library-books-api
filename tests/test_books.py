def test_create_book(client):
    r = client.post("/books", json={"title": "Dune", "author": "Frank Herbert", "year": 1965})
    assert r.status_code == 201
    assert r.json()["id"] == 1
    assert r.json()["title"] == "Dune"


def test_list_books(client, book):
    assert client.get("/books").json() == [book]


def test_list_books_empty(client):
    assert client.get("/books").json() == []
