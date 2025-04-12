from typing import Any, Generator


def filter_by_currency(
        list_of_transactions: list[dict[str, Any]], code="USD"
) -> Generator[dict[str, Any], None, None]:
    for list_of_currencies in list_of_transactions:
        if (
                list_of_currencies.get("operationAmount", {})
                        .get("currency", {})
                        .get("code")
                == code
        ):
            yield list_of_currencies


def transaction_descriptions(
        list_dictionaries_transactions: list[dict[str, Any]]
) -> Generator[str, None, None]:
    for description_operation in list_dictionaries_transactions:
        key = description_operation.get("description")
        if key:
            yield key


def card_number_generator(start: int, end: int) -> str:
    for i in range(start, end + 1):
        count_0 = str(i).zfill(16)
        yield count_0
