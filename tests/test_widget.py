from src.widget import mask_account_card


def test_mask_account_card(account_name_numbers):
    assert mask_account_card("Visa Platinum 7000792289606361") == account_name_numbers
