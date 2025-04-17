import json
from datetime import datetime as dt
from datetime import timedelta

def check_capacity(max_capacity: int, guests: list) -> bool:
    start_date = min(set([dt.strptime(i['check-in'], '%Y-%m-%d') for i in guests]))  # дата заезда первого клиента
    end_date = max(set([dt.strptime(i['check-out'], '%Y-%m-%d') for i in guests]))  # дата последнего выселения
    date_dict = {dt.strftime((start_date + timedelta(n)), '%Y-%m-%d'): 0 for n in
                 range(int((end_date - start_date).days) + 1)}

    for guest in guests:
        check_in = dt.strptime(guest['check-in'], '%Y-%m-%d')
        check_out = dt.strptime(guest['check-out'], '%Y-%m-%d')
        if (check_out - check_in).days == 0:
            date_dict[guest['check-in']] = 1
        else:
            for d in [dt.strptime(guest["check-in"], '%Y-%m-%d') + timedelta(n) for n in
                      range((dt.strptime(guest["check-out"], '%Y-%m-%d') - dt.strptime(guest["check-in"],
                                                                                       '%Y-%m-%d')).days)]:
                date_dict[dt.strftime(d, '%Y-%m-%d')] += 1

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
