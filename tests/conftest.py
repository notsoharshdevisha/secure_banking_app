import pytest
from app import create_app
from flask import Flask
from flask.testing import FlaskClient
from bin.create_test_db import create_test_db
from bin.destroy_test_db import destroy_test_db
from typing import Generator


@pytest.fixture()
def app() -> Generator[Flask, None, None]:
    app: Flask = create_app()
    app.config.update({
        "TESTING": True
    })

    create_test_db()

    yield app

    destroy_test_db()


@pytest.fixture()
def client(app: Flask):
    with app.app_context():
        # Use the app's test client for testing
        client = app.test_client()
        yield client
