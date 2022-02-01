# Все фильтры должны возвращать булево значение(True если данные проходят фильтр) и tuple из пары ключ-значение,
# обработанные согласно фильтру(если необходимо). Все фильтры ожидают пару str-int, согласно условию

def filter_even_values(key: str, value: int):
    """
    Фильтр возвращает записи словаря с чётными значениями
    :param key: ключ
    :param value: значение
    :return: статус фильтра(прошла ли запись фильтр) и данные с нужной обработкой
    """
    return_key, return_value = key, value

    if value % 2 == 0:
        status = True
    else:
        status = False

    return status, (return_key, return_value)


def filter_alpha_keys(key: str, value: int):
    """
    Фильтр возвращает записи словаря с ключами из букв
    :param key: ключ
    :param value: значение
    :return: статус фильтра(прошла ли запись фильтр) и данные с нужной обработкой
    """
    status = key.isalpha()
    return_key, return_value = key.lower(), value

    return status, (return_key, return_value)


def filter_available_values(key, value):
    """
    Фильтр возвращает записи словаря с не None значениями
    :param key: ключ
    :param value: значение
    :return: статус фильтра(прошла ли запись фильтр) и данные с нужной обработкой
    """
    return_key, return_value = key, value

    if value % 2 == 0:
        status = True
    else:
        status = False

    return status, (return_key, return_value)
