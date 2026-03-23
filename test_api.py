import pytest
from main import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_ac_not_valid_c_cannot_follow_a(client):
    resp = client.post("/validate", json={"word": "ac"})
    data = resp.get_json()
    assert data["valid"] is False
    assert "cannot follow" in data["reason"]


def test_ab_not_valid_b_cannot_be_final(client):
    resp = client.post("/validate", json={"word": "ab"})
    data = resp.get_json()
    assert data["valid"] is False
    assert "cannot be the final letter" in data["reason"]


def test_aba_valid(client):
    resp = client.post("/validate", json={"word": "aba"})
    data = resp.get_json()
    assert data["valid"] is True
