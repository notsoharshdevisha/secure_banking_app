from services.user_service import get_user_with_credentials, logged_in
import pytest
from unittest import mock
from flask import request, g
from utils import create_token


@pytest.mark.service
def test_get_user_with_cred_service(app_with_session_scope):
    with app_with_session_scope.app_context():
        assert get_user_with_credentials('lol', '123456') is None
        assert get_user_with_credentials('alice@example.com', '3456') is None
        assert get_user_with_credentials(
            'alice@example.com', '123456') is not None


@pytest.mark.service
def test_logged_in_service(app_with_session_scope):
    user = 'alice@example.com'

    with app_with_session_scope.app_context():
        token = create_token(user)
        with app_with_session_scope.test_request_context(path='/', headers={'Cookie': f'auth_token={token}'}):
            g.user = user
            assert logged_in()

        with app_with_session_scope.test_request_context(path='/'):
            g.user = user
            assert not logged_in()
