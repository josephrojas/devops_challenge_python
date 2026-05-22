import pytest
from fastapi.testclient import TestClient

from src.api import app

client = TestClient(app)


@pytest.fixture
def costs():
    return {"socks": 5, "shoes": 60, "sweater": 30}


def test_calculate_total_basic(costs):
    """Test basic calculation with existing items and tax."""
    response = client.post(
        "/total",
        json={"costs": costs, "items": ["socks", "shoes"], "tax": 0.09},
    )
    assert response.status_code == 200
    assert response.json()["result"] == 70.85


def test_calculate_total_missing_item_ignored(costs):
    """Test that items not in costs are ignored."""
    response = client.post(
        "/total",
        json={"costs": costs, "items": ["socks", "banana"], "tax": 0.09},
    )
    assert response.status_code == 200
    assert response.json()["result"] == 5.45


def test_calculate_total_empty_items(costs):
    """Test that empty items list returns 0.00."""
    response = client.post(
        "/total",
        json={"costs": costs, "items": [], "tax": 0.09},
    )
    assert response.status_code == 200
    assert response.json()["result"] == 0.0


def test_calculate_total_invalid_payload():
    """Test that invalid payload returns 422."""
    response = client.post(
        "/total",
        json={"costs": "not a dict", "items": [], "tax": 0.09},
    )
    assert response.status_code == 422