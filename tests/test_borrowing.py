def test_borrow_book(client, book):
    r = client.post(f"/books/{book['id']}/borrow", json={"borrower": "Ivan"})
    assert r.status_code == 200
    assert r.json()["is_borrowed"] is True
    assert r.json()["borrower"] == "Ivan"


def test_borrow_already_borrowed_book(client, book):
    client.post(f"/books/{book['id']}/borrow", json={"borrower": "Ivan"})
    r = client.post(f"/books/{book['id']}/borrow", json={"borrower": "Maria"})
    assert r.status_code == 409


def test_borrow_missing_book(client):
    assert client.post("/books/999/borrow", json={"borrower": "Ivan"}).status_code == 404


def test_return_book(client, book):
    client.post(f"/books/{book['id']}/borrow", json={"borrower": "Ivan"})
    r = client.post(f"/books/{book['id']}/return")
    assert r.status_code == 200
    assert r.json()["is_borrowed"] is False
    assert r.json()["borrower"] is None


def test_return_book_that_is_not_borrowed(client, book):
    assert client.post(f"/books/{book['id']}/return").status_code == 409


def test_return_missing_book(client):
    assert client.post("/books/999/return").status_code == 404
