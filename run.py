import json
from datetime import datetime as dt
from datetime import timedelta


def check_capacity(max_capacity: int, guests: list) -> bool:
    date_dict = {}
    for guest in guests:
        check_in = dt.strptime(guest['check-in'], '%Y-%m-%d')
        check_out = dt.strptime(guest['check-out'], '%Y-%m-%d')
        if (check_out - check_in).days == 0:
            date_dict[guest['check-in']] = 1
        else:
            for d in [check_in + timedelta(n) for n in range((check_out - check_in).days)]:
                delta = d.strftime('%Y-%m-%d')
                if delta in date_dict:
                    date_dict[delta] += 1
                else:
                    date_dict[delta] = 1
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
