from services.account_service import get_balance, do_transfer
from utils import Transaction
import pytest


@pytest.mark.service
def test_get_balance_service(app_with_functional_scope):
    with app_with_functional_scope.app_context():
        assert 7500 == get_balance('1234567890', 'alice@example.com')


@pytest.mark.service
def test_do_transfer_service(app_with_functional_scope):
    transaction = Transaction("1234567890", "3456789012", "200")
    with app_with_functional_scope.app_context():
        do_transfer(transaction)
        assert 7300 == get_balance('1234567890', 'alice@example.com')
        assert 3200 == get_balance('3456789012', 'bob@example.com')
