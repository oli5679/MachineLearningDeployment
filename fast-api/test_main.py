import pytest
import main
import json
from fastapi.testclient import TestClient


INPUT = {"input": [{"Male": 0, "Age": 21, "SibSp": 0, "Parch": 0, "Fare": 21.5}]}

EXPECTED_OUTPUT = 0.7801685773985715


@pytest.fixture
def client():
    yield TestClient(main.app)


def test_healthcheck(client):
    """Check correct status code for healthcheck"""

    response = client.get("/")
    assert response.status_code == 200


def test_422_if_empty_post(client):
    """Check 422 if empty post request"""
    response = client.post("/score/")
    assert response.status_code == 422


def test_create_score(client):
    """
    Check correct response for input
    """
    response = client.post("/score/", json=INPUT)
    score = score = response.json()[0]["prediction"]
    assert score == pytest.approx(EXPECTED_OUTPUT)
