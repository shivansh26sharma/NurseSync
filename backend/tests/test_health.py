def test_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "NurseSync" in response.json()["message"]


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_health_db(client):
    response = client.get("/health/db")
    assert response.status_code == 200
    assert response.json()["database"] == "connected"
