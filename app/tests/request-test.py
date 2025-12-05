import pytest
from app.main import app

with app.test_client() as client:


    def test_health_endpoint(): #Test Health Endpoint
        response = client.get('/health')
        assert response.status_code == 200
        assert response.data.decode() == 'Server health'

    def test_get_orders_endpoint(): #Test Get Orders Endpoint
        response = client.get('/orders')
        assert response.status_code == 200
        data = response.get_json()
        assert 'orders' in data
        assert isinstance(data['orders'], list)

    def test_post_orders_endpoint(): #Test Post Orders Endpoint
        new_order = {'item': 'teste-endpoint', 'quantity': 3}
        response = client.post('/orders', json=new_order)
        assert response.status_code == 201
        data = response.get_json()
        assert 'new_order' in data
        assert data['new_order']['item'] == 'teste-endpoint' #verify item
        assert data['new_order']['quantity'] == 3 #verify quantity
        assert 'orders' in client.get('/orders').get_json() #verify order added to list