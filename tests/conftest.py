import pytest
from app import create_app
from bin.create_test_db import create_test_db
from bin.destroy_test_db import destroy_test_db
from utils import create_token
from services.user_service import logged_in
from flask import redirect, request


@pytest.fixture(scope='session')
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "DB": 'test_bank.db'
    })

    @app.before_request
    def check_auth():
        if request.path != "/login" and not logged_in():
            return redirect("/login")

    create_test_db()

    yield app

    destroy_test_db()


@pytest.fixture(scope='session')
def unauthenticated_client(app):
    # Use the app's test client for testing
    return app.test_client()


@pytest.fixture(scope='session')
def authenticated_client(app):
    client = app.test_client()
    with app.app_context():
        token = create_token('alice@example.com')
        client.set_cookie('auth_token', token)
    return client
