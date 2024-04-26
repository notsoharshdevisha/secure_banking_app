from bs4 import BeautifulSoup
import pytest


@pytest.mark.api_endpoint
def test_login_api(unauthenticated_client_with_functional_scope):
    response = unauthenticated_client_with_functional_scope.get('/login')
    soup = BeautifulSoup(response.data, 'html.parser')
    csrf_token = soup.find('input', {'name': 'csrf_token'})['value']
    good_data = {
        'email': 'alice@example.com',
        'password': '123456',
        'csrf_token': csrf_token
    }
    bad_data = {
        'email': 'lol',
        'password': 'hehe',
        'csrf_token': csrf_token
    }

    assert unauthenticated_client_with_functional_scope.get_cookie(
        'auth_token') == None

    response = unauthenticated_client_with_functional_scope.post('/login')
    assert response.status_code == 200
    assert 'Email' in response.text
    assert 'Password' in response.text
    assert response.request.path == '/login'

    response = unauthenticated_client_with_functional_scope.post(
        '/login', data=bad_data)
    assert response.status_code == 200
    assert 'Email' in response.text
    assert 'Password' in response.text
    assert response.request.path == '/login'

    response = unauthenticated_client_with_functional_scope.post(
        '/login', data=good_data)
    assert unauthenticated_client_with_functional_scope.get_cookie(
        'auth_token') != None
    assert response.status_code == 302


@pytest.mark.api_endpoint
def test_transfer_api(authenticated_client_with_functional_scope):
    route = '/transfer'
    valid_data = {
        'source': '1234567890',
        'target': '3456789012',
        'amount': '200'
    }

    invalid_data = {
        'source': '4567890',
        'target': '3456789012',
        'amount': '200'
    }

    response = authenticated_client_with_functional_scope.post(route)
    assert response.status_code == 400

    response = authenticated_client_with_functional_scope.post(
        route, data=invalid_data)
    assert response.status_code == 400

    response = authenticated_client_with_functional_scope.post(
        route, data=valid_data)
    assert response.status_code == 302
