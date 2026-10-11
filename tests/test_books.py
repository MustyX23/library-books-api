def test_create_book(client):
    r = client.post("/books", json={"title": "Dune", "author": "Frank Herbert", "year": 1965})
    assert r.status_code == 201
    assert r.json()["id"] == 1
    assert r.json()["title"] == "Dune"
