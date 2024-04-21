from services.user_service import logged_in
from flask import request
from bs4 import BeautifulSoup


def test_login_view(client) -> None:
    response = client.get("/login")
    assert "Email:" in response.text
    assert "Password:" in response.text
    assert response.status_code in [200, 302]


def test_login_api(client) -> None:
    response = client.get('/login')
    soup = BeautifulSoup(response.data, "html.parser")
    csrf_token = soup.find('input', {'name': 'csrf_token'})['value']
    form_data = {
        'email': 'alice@example.com',
        'password': '123456',
        'csrf_token': csrf_token
    }
    assert client.get_cookie('auth_token') == None
    response = client.post("/login",  data=form_data)
    assert client.get_cookie('auth_token') != None
    assert response.status_code == 303
