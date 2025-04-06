import pytest


@pytest.fixture
def card_numbers():
    return ("7000 79** **** 6361")

@pytest.fixture
def account_numbers():
    return ("**4305")

@pytest.fixture
def account_name_numbers():
    return ("VisaPlatinum 7000 79** **** 6361")
