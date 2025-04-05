import pytest

from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number(card_numbers):
    assert get_mask_card_number("7000792289606361") == card_numbers


def test_get_mask_card_number_letters():
    with pytest.raises(ValueError):
        get_mask_card_number("7ooo792289606361")


def test_get_mask_card_number_empty_list():
    with pytest.raises(ValueError):
        assert get_mask_card_number("")


def test_get_mask_account(account_numbers):
    assert get_mask_account("73654108430135874305") == account_numbers


def test_get_mask_account_letters():
    with pytest.raises(ValueError):
        assert get_mask_account("736541o84301358743o5")


def test_get_mask_account_empty_list():
    with pytest.raises(ValueError):
        assert get_mask_account("")
