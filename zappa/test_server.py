import pytest
import server
import json

INPUT = {"input": [{"Male": 0, "Age": 21, "SibSp": 0, "Parch": 0, "Fare": 21.5}]}

EXPECTED_OUTPUT = 0.7801685773985715


@pytest.fixture
def client():
    yield server.app.test_client()


def test_healthcheck(client):
    """Check correct status code for healthcheck"""

    response = client.get("/")
    assert response.status_code == 200


def test_404_if_empty_post(client):
    """Check 404 if empty post request"""
    response = client.post("/")
    assert response.status_code == 404


def test_create_score(client):
    """
    Check correct response for input
    """
    response = client.post(json=INPUT)
    score = json.loads(response.data)[0]["prediction"]
    assert score == pytest.approx(EXPECTED_OUTPUT)
