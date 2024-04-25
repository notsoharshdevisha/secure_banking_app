from utils import Transaction
import pytest


@pytest.mark.isolated
def test_transaction_class_init():
    try:
        Transaction('123', "1234567890", "1000")
        assert True == False
    except Exception as error:
        assert str(error) == "Bad arguments"

    try:
        Transaction('1234567890', "123", "1000")
        assert True == False
    except Exception as error:
        assert str(error) == "Bad arguments"

    try:
        Transaction('3456789012', "1234567890", "1001")
        assert True == False
    except Exception as error:
        assert str(error) == "Bad arguments"

    try:
        Transaction('3456789012', "1234567890", "-12")
        assert True == False
    except Exception as error:
        assert str(error) == "Bad arguments"

    try:
        Transaction('1234567890', "1234567890", "100")
        assert True == False
    except Exception as error:
        assert str(error) == "Bad arguments"
