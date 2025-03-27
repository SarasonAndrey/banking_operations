def get_mask_card_number(card_number: str) -> str:
    if len(card_number) != 16 or not card_number.isdigit():
        raise ValueError("Номер карты должен состоять из 16 цифр.")
    return (
        card_number[0:4]
        + " "
        + card_number[4:6]
        + "**"
        + " "
        + "****"
        + " "
        + card_number[-4:]
    )


def get_mask_account(mask_account: str) -> str:
    if len(mask_account) != 20 or not mask_account.isdigit():
        raise ValueError("Номер счета должен состоять из 20 цифр.")
    return "**" + mask_account[-4:]
