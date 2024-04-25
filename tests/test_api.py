from bs4 import BeautifulSoup
import pytest


@pytest.mark.api_endpoint
def test_login_api(unauthenticated_client_with_functional_scope):
    response = unauthenticated_client_with_functional_scope.get('/login')
    soup = BeautifulSoup(response.data, 'html.parser')
    csrf_token = soup.find('input', {'name': 'csrf_token'})['value']
    data = {
        'email': 'alice@example.com',
        'password': '123456',
        'csrf_token': csrf_token
    }

    assert unauthenticated_client_with_functional_scope.get_cookie(
        'auth_token') == None

    response = unauthenticated_client_with_functional_scope.post('/login')
    assert response.status_code == 200
    assert 'Email' in response.text
    assert 'Password' in response.text
    assert response.request.path == "/login"

    response = unauthenticated_client_with_functional_scope.post(
        '/login', data=data)
    assert unauthenticated_client_with_functional_scope.get_cookie(
        'auth_token') != None
    assert response.status_code == 302

    unauthenticated_client_with_functional_scope.delete_cookie('auth_token')

