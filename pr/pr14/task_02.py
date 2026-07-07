""" 02 Генератор случайных дат

Создайте генератор, который
- генерирует случайные даты в пределах одного года.

Генератор должен
- принимать год в качестве аргумента
- и выдавать следующую случайную дату при каждом вызове, учитывая
    - количество дней в месяце,
    - а также високосные годы.

Пример вывода:
2025-11-04
2025-01-24
2025-05-08
2025-04-05
2025-12-04
"""

import random
random.seed(42)

def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def random_dates(year):
    days = {
        1: 31,
        2: 29 if is_leap(year) else 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }
    while True:
        month = random.randint(1, 12)
        day = random.randint(1, days[month])
        yield f'{year}-{month:02}-{day:02}'

if __name__ == "__main__":
    gen = random_dates(2025)

    for _ in range(5):
        print(next(gen))



