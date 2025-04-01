from operator import itemgetter


def filter_by_state(list_dictionaries: list, state="EXECUTED") -> list:
    new_list_dictionaries = []
    for i in list_dictionaries:
        if i["state"] == state:
            new_list_dictionaries.append(i)
    return new_list_dictionaries


def sort_by_date(list_dictionaries: list) -> list:
    for i in list_dictionaries:
        new_list_sort_by_date = sorted(
            list_dictionaries, key=itemgetter("date"), reverse=True
        )
    return new_list_sort_by_date
