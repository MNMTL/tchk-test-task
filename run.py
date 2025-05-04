import json
from datetime import datetime as dt
from datetime import timedelta


def check_capacity(max_capacity: int, guests: list) -> bool:
    date_dict = {}
    for guest in guests:
        check_in = dt.strptime(guest['check-in'], '%Y-%m-%d')
        check_out = dt.strptime(guest['check-out'], '%Y-%m-%d')
        days = (check_out - check_in).days
        if days < 0:
            raise ValueError(f'Некорректные даты: {guest}')

        elif days in [0, 1]:
            date_dict[guest['check-in']] = date_dict.get(guest['check-in'], 0) + 1

        else:
            for d in (check_in + timedelta(n) for n in range(int(days))):
                delta = d.strftime('%Y-%m-%d')
                date_dict[delta] = date_dict.get(delta, 0) + 1

    if max_capacity >= max(date_dict.values()):
        return True
    else:
        return False


if __name__ == "__main__":
    # Чтение входных данных
    # Первая строка - вместимость гостиницы
    max_capacity = int(input())
    # Вторая строка - количество записей о гостях
    n = int(input())

    guests = []
    # Читаем n строк, json-данные о посещении.
    for _ in range(n):
        guest = json.loads(input())
        guests.append(guest)

    # Вызов функции
    result = check_capacity(max_capacity, guests)
    # Вывод результата
    print(result)
