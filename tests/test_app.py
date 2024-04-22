from services.user_service import logged_in
from flask import request, g
from bs4 import BeautifulSoup
def test_home_route(client) -> None:
    response = client.get('/')
    assert response.status_code == 302


def test_login_view(client) -> None:
    response = client.get('/login')
    assert 'Email:' in response.text
    assert 'Password:' in response.text
    assert response.status_code in [200, 302]


def test_login_api(client) -> None:
    response = client.get('/login')
    soup = BeautifulSoup(response.data, 'html.parser')
    csrf_token = soup.find('input', {'name': 'csrf_token'})['value']
    form_data = {
        'email': 'alice@example.com',
        'password': '123456',
        'csrf_token': csrf_token
    }
    assert client.get_cookie('auth_token') == None
    response = client.post('/login',  data=form_data)
    assert client.get_cookie('auth_token') != None
    assert response.status_code == 303


def test_dashboard_view(client) -> None:
    g.user = 'alice@example.com'
    response = client.get('/dashboard')
    assert response.status_code == 200


def test_details_view(client) -> None:
    g.user = 'alice@example.com'
    response = client.get('/details')
    assert response.status_code == 400
    response = client.get('/details?account=100')
    assert response.status_code == 200
    assert g.user in response.text
    assert 'Details for Account' in response.text
    assert 'Your balance is' in response.text


def test_logout_api(client) -> None:
    client.set_cookie('auth_token', 'dummy_token')
    assert client.get_cookie('auth_token') != None
    client.get('/logout')
    assert client.get_cookie('auth_token') == None


def test_transfer_view(client) -> None:
    response = client.get('/transfer')
    assert response.status_code == 200
    response_text = response.text
    assert 'From' in response_text
    assert 'To' in response_text
    assert 'Amount' in response_text
