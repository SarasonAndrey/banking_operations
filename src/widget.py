from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(name_number: str) -> str:
    name_card = ""
    number_card = ""
    for i in name_number.split():

        if i.isalpha():
            name_card += i
        else:
            number_card += i
            if "Счет" in name_card:
                return f"{name_card} {get_mask_account(name_number)}"
    return f"{name_card} {get_mask_card_number(number_card)}"


def get_date(date_string):
    try:
        date_obj = datetime.fromisoformat(date_string)
        return date_obj.strftime("%d.%m.%Y")
    except ValueError as e:
        raise ValueError(f"Неверный формат даты: {e}")
