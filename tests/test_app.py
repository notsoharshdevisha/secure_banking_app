from services.user_service import logged_in


def test_login_view(client) -> None:
    response = client.get("/login")
    with client.application.test_request_context():
        if logged_in():
            assert response.status_code == 303
        else:
            assert response.status_code == 200
