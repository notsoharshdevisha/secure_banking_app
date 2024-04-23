from flask import g


def test_login_view(authenticated_client):
    response = authenticated_client.get('/login')
    assert response.status_code == 302


def test_dashboard_view(app, authenticated_client) -> None:
    with app.app_context():
        g.user = 'alice@example.com'
        response = authenticated_client.get('/dashboard')
        assert response.status_code == 200


def test_details_view(app, authenticated_client) -> None:
    with app.app_context():
        g.user = 'alice@example.com'
        response = authenticated_client.get('/details')
        assert response.status_code == 400
        response = authenticated_client.get('/details?account=100')
        assert response.status_code == 200
        assert g.user in response.text
        assert 'Details for Account' in response.text
        assert 'Your balance is' in response.text


def test_transfer_view(authenticated_client) -> None:
    response = authenticated_client.get('/transfer')
    assert response.status_code == 200
    response_text = response.text
    assert 'From' in response_text
    assert 'To' in response_text
    assert 'Amount' in response_text


def test_logout_api(authenticated_client) -> None:
    assert authenticated_client.get_cookie('auth_token') != None
    authenticated_client.get('/logout')
    assert authenticated_client.get_cookie('auth_token') == None
