from flask import g
import pytest


@pytest.mark.view
def test_login_view(authenticated_client_with_session_scope):
    response = authenticated_client_with_session_scope.get('/login')
    assert response.status_code == 302


@pytest.mark.view
def test_dashboard_view(app_with_session_scope, authenticated_client_with_session_scope) -> None:
    with app_with_session_scope.app_context():
        g.user = 'alice@example.com'
        response = authenticated_client_with_session_scope.get('/dashboard')
        assert response.status_code == 200


@pytest.mark.view
def test_details_view(app_with_session_scope, authenticated_client_with_session_scope) -> None:
    with app_with_session_scope.app_context():
        g.user = 'alice@example.com'
        response = authenticated_client_with_session_scope.get('/details')
        assert response.status_code == 400
        response = authenticated_client_with_session_scope.get(
            '/details?account=100')
        assert response.status_code == 200
        assert g.user in response.text
        assert 'Details for Account' in response.text
        assert 'Your balance is' in response.text


@pytest.mark.view
def test_transfer_view(authenticated_client_with_session_scope) -> None:
    response = authenticated_client_with_session_scope.get('/transfer')
    assert response.status_code == 200
    response_text = response.text
    assert 'From' in response_text
    assert 'To' in response_text
    assert 'Amount' in response_text


@pytest.mark.view
def test_logout_api(authenticated_client_with_session_scope) -> None:
    assert authenticated_client_with_session_scope.get_cookie(
        'auth_token') != None
    authenticated_client_with_session_scope.get('/logout')
    assert authenticated_client_with_session_scope.get_cookie(
        'auth_token') == None
