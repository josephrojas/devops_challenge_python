from fastapi.testclient import TestClient

from src.api import app

client = TestClient(app)


def test_nth_letter_basic():
    """Test basic case from exercise description."""
    response = client.post("/nth", json={"words": ["yoda", "best", "has"]})
    assert response.status_code == 200
    assert response.json()["result"] == "yes"


def test_nth_letter_empty_list():
    """Test that empty list returns empty string."""
    response = client.post("/nth", json={"words": []})
    assert response.status_code == 200
    assert response.json()["result"] == ""


def test_nth_letter_word_too_short():
    """Test that words shorter than their position are ignored."""
    response = client.post("/nth", json={"words": ["yoda", "b", "has"]})
    assert response.status_code == 200
    assert response.json()["result"] == "ys"


def test_nth_letter_invalid_payload():
    """Test that invalid payload returns 422."""
    response = client.post("/nth", json={"words": "not a list"})
    assert response.status_code == 422