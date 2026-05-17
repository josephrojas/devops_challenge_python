from fastapi.testclient import TestClient

from src.api import app

client = TestClient(app)

def test_add_entry():
    response = client.post("/entries?word=Apple&definition=A fruit")
    assert response.status_code == 200

def test_look_existing_entry():
    client.post("/entries?word=Apple&definition=A fruit")
    response = client.get("/entries/Apple")
    assert response.status_code == 200
    assert response.json()["result"] == "A fruit"

def test_look_missing_entry():
    response = client.get("/entries/Banana")
    assert response.status_code == 200
    assert "Can't find entry for Banana" in response.json()["result"]