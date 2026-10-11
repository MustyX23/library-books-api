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
