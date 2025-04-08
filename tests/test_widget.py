import pytest

from src.widget import get_date, mask_account_card


def test_mask_account_card(account_name_numbers):
    assert mask_account_card("Visa Platinum 7000792289606361") == account_name_numbers


def test_mask_account_card_letters(account_name_numbers):
    with pytest.raises(ValueError):
        mask_account_card("Visa Platinum 7ooo792289606361")


def test_mask_account_card_non_name(account_name_numbers):
    with pytest.raises(ValueError):
        mask_account_card("7000792289606361")


def test_mask_account_card_empty_list():
    with pytest.raises(ValueError):
        mask_account_card("")


def test_get_date():
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"


def test_get_date_not_format():
    with pytest.raises(ValueError):
        get_date("11-03-2024T02:26:18.671407")


def test_get_date_non():
    with pytest.raises(ValueError):
        get_date("")
