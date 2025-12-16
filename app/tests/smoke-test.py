import pytest, requests

url = "http://127.0.0.1:5000"

def test_get_health():
    response = requests.get(f"{url}/health")
    assert response.status_code == 200
    assert "Server health"

def test_get_orders():
    response = requests.get(f"{url}/orders")
    assert response.status_code == 200

def test_post_order():
    new_order = {"item": "Smoke Test", "quantity": 5}
    response = requests.post(f"{url}/orders", json=new_order)
    assert response.status_code == 201
    response_data = response.json()
    assert "new_order" in response_data
    assert response_data["new_order"]["item"] == new_order["item"]
    assert response_data["new_order"]["quantity"] == new_order["quantity"]
    assert "id" in response_data["new_order"]