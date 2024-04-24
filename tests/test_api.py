from bs4 import BeautifulSoup


def test_login_api(unauthenticated_client):
    response = unauthenticated_client.get('/login')
    soup = BeautifulSoup(response.data, 'html.parser')
    csrf_token = soup.find('input', {'name': 'csrf_token'})['value']
    data = {
        'email': 'alice@example.com',
        'password': '123456',
        'csrf_token': csrf_token
    }
    assert unauthenticated_client.get_cookie('auth_token') == None
    response = unauthenticated_client.post('/login')
    assert response.status_code == 200
    assert 'Email' in response.text
    assert 'Password' in response.text
    assert response.request.path == "/login"
    response = unauthenticated_client.post('/login', data=data)
    assert unauthenticated_client.get_cookie('auth_token') != None
    assert response.status_code == 302

    unauthenticated_client.delete_cookie('auth_token')
