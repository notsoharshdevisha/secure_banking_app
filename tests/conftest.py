import pytest
from app_factory import create_app
from bin.create_test_db import create_test_db
from bin.destroy_test_db import destroy_test_db
from utils import create_token
from services.user_service import logged_in
from flask import redirect, request
from middlewares import check_auth


@pytest.fixture(scope='session')
def app_with_session_scope():
    create_test_db()

    yield create_test_app()

    destroy_test_db()


@pytest.fixture(scope='session')
def unauthenticated_client_with_session_scope(app_with_session_scope):
    # Use the app's test client for testing
    return app_with_session_scope.test_client()


@pytest.fixture(scope='session')
def authenticated_client_with_session_scope(app_with_session_scope):
    client = app_with_session_scope.test_client()
    with app_with_session_scope.app_context():
        token = create_token('alice@example.com')
        client.set_cookie('auth_token', token)
    return client


@pytest.fixture(scope="function")
def app_with_functional_scope():
    create_test_db()

    yield create_test_app()

    destroy_test_db()


@pytest.fixture(scope="function")
def unauthenticated_client_with_functional_scope(app_with_functional_scope):
    # Use the app's test client for testing
    return app_with_functional_scope.test_client()


@pytest.fixture(scope="function")
def authenticated_client_with_functional_scope(app_with_functional_scope):
    client = app_with_functional_scope.test_client()
    with app_with_functional_scope.app_context():
        token = create_token('alice@example.com')
        client.set_cookie('auth_token', token)
    return client


def create_test_app():
    app = create_app()

    app.config.update({
        'TESTING': True,
        'DB': 'test_bank.db'
    })

    check_auth(app)

    return app
