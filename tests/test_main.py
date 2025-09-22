from fastapi.testclient import TestClient
from src.main import api   
client = TestClient(api)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Message": "Welcome to the Ticket Booking System"}


def test_create_ticket():
    response = client.post("/ticket", json={
        "id": 1,
        "flight_name": "Air BD",
        "flight_date": "2025-10-15",
        "flight_time": "14:30",
        "destination": "Dhaka"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["flight_name"] == "Air BD"
    assert data["destination"] == "Dhaka"


def test_get_tickets():
    response = client.get("/ticket")
    assert response.status_code == 200
    tickets = response.json()
    assert isinstance(tickets, list)
    assert len(tickets) > 0
    assert tickets[0]["id"] == 1


def test_update_ticket():
    response = client.put("/ticket/1", json={
        "id": 1,
        "flight_name": "Air BD Updated",
        "flight_date": "2025-10-16",
        "flight_time": "15:30",
        "destination": "Chittagong"
    })
    assert response.status_code == 200
    updated = response.json()
    assert updated["flight_name"] == "Air BD Updated"
    assert updated["destination"] == "Chittagong"


def test_delete_ticket():
    response = client.delete("/ticket/1")
    assert response.status_code == 200
    deleted = response.json()
    assert deleted["id"] == 1
    assert deleted["flight_name"] == "Air BD Updated"
