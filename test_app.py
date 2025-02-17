import pytest
from app import app

@pytest.fixture
def client():
    """Creates a test client for the Flask app."""
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_homepage(client):
    """Tests if the homepage loads successfully and contains expected content."""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Welcome to My Flask App" in response.data  # ✅ Checking if the HTML contains the expected heading
    assert b"Flask is awesome!" in response.data       # ✅ Checking the paragraph text
