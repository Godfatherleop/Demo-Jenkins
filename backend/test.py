from app import app

def test_index():
    client = app.test_client()
    response = client.get("/quote")
    assert response.status_code == 200
    assert "quote" in response.get_json()
