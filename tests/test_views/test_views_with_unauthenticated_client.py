import pytest


@pytest.mark.view
def test_login_view(unauthenticated_client_with_session_scope):
    response = unauthenticated_client_with_session_scope.get('/login')
    assert response.status_code == 200


@pytest.mark.view
def test_dashboard_view(unauthenticated_client_with_session_scope) -> None:
    response = unauthenticated_client_with_session_scope.get('/dashboard')
    assert response.status_code == 302


@pytest.mark.view
def test_details_view(unauthenticated_client_with_session_scope) -> None:
    response = unauthenticated_client_with_session_scope.get('/details')
    assert response.status_code == 302


@pytest.mark.view
def test_transfer_view(unauthenticated_client_with_session_scope) -> None:
    response = unauthenticated_client_with_session_scope.get('/transfer')
    assert response.status_code == 302
