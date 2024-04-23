def test_login_view(unauthenticated_client):
    response = unauthenticated_client.get('/login')
    assert response.status_code == 200


def test_dashboard_view(unauthenticated_client) -> None:
    response = unauthenticated_client.get('/dashboard')
    assert response.status_code == 302


def test_details_view(unauthenticated_client) -> None:
    response = unauthenticated_client.get('/details')
    assert response.status_code == 302


def test_transfer_view(unauthenticated_client) -> None:
    response = unauthenticated_client.get('/transfer')
    assert response.status_code == 302
