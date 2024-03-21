from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_get_digimon():
    """
    Test to get digimon 
    Expect the response to be a 200 (OK)
    """
    response = client.get("/api/digimon")
    assert response.status_code == 200
    assert response.json()["message"] == "Digimon data stored correctly in the database"


def test_get_digimon_by_id():
    """
    Test get digimon by ID
    Expect the response to be a 200 (OK)
    """
    response = client.get("/api/digimon/1")
    assert response.status_code == 200
    assert "id" in response.json()


def test_add_digimon():
    """
    Test adding a new digimon into the database
    Expect the response to be a 200 (Created)
    """
    digimon_data = {
        "name": "Agumon",
        "img": "https://example.com/agumon.jpg",
        "lvl": "Rookie"
    }
    response = client.post("/api/data", json=digimon_data)
    assert response.status_code == 200
    assert response.json()["message"] == "Digimon successfully added to database"


def test_get_nonexistent_digimon():
    """
    Test get a digimon id nonexistent
    Expect the response to be a 404 (Not Found)
    """
    response = client.get("/api/digimon/999")
    assert response.status_code == 404
    assert "error" in response.json()


def test_add_invalid_digimon_data():
    """
    Test get a digimon with incomplete data "Without name field"
    Expect the response to be a 422 Unprocessable Entity error (for unprocessable data)
    """
    invalid_digimon_data = {
        "img": "https://example.com/agumon.jpg",
        "lvl": "Rookie"
    }
    response = client.post("/api/data", json=invalid_digimon_data)
    assert response.status_code == 422
    assert "validation error" in response.json()
