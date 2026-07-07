# """ 01 Сумма чисел списка
#
# Напишите рекурсивную функцию, которая
# - вычисляет сумму всех чисел в списке.
#
# Функция должна проверять:
# - Аргумент должен быть списком.
# - Все элементы списка должны быть числами.
#
# Если данные не валидны необходимо выбрасывать исключение.
# При вызове функции обработайте возможное исключение.
#
# Данные:
# numbers = [1, 2, 3, 4, 5]
# Пример вывода:
# 15
# """
#
# def recursive_sum(lst):
#     pass
#
# try:
#     pass
# except ...:
#     pass
# """ 02 Реверс строки
#
# Напишите рекурсивную функцию, которая
# - переворачивает строку.
#
# Если передан не строковый тип, выбросить исключение.
# При вызове функции обработайте возможное исключение.
#
# Данные:
# text = "recursion"
# Пример вывода:
# noisrucer
# """
#
# def reverse_string(s):
#     pass
#
# try:
#     pass
# except ...:
#     pass
""" 03 Глубина вложенности списка

Напишите рекурсивную функцию, которая
- определяет максимальную глубину вложенности списка.

Функция должна проверять:
- Аргумент должен быть списком.
- Вложенные структуры, если они есть, также должны быть списками.
- Если данные не валидны необходимо выбрасывать исключение.

При вызове функции обработайте возможное исключение.

Данные:
nested_list = [1, [2, [3, [4, [5]]]], 6, [[7, 8], 9]]

Пример вывода:
Максимальная глубина: 5
"""

def max_depth(data):
    if not isinstance(data, list):
        raise TypeError('Аргумент должен быть списком.')
    return 1 + max([max_depth(d) for d in data if isinstance(d, list)])
try:
    nested_list = [1, [2, [3, [4, [5]]]], 6, [[7, 8], 9]]
    print(f"Максимальная глубина: {max_depth(nested_list)}")
except TypeError as e:
    print(f"Ошибка{e}")
""" 04 Сумма продаж

Есть дерево подразделений внутри компании
(каждое подразделение может содержать «дочерние» отделы).
Напишите рекурсивную функцию, которая
- подсчитывает суммарные продажи для всех отделов.

Функция должна проверять:
- Аргумент должен быть словарем.
- Дочерние отделы (если есть) должны быть списком словарей.

Если данные не валидны необходимо выбрасывать исключение.
При вызове функции обработайте возможное исключение.

Данные:
company_structure = {
    "dept_name": "Head Office",
    "sales": 100,
    "sub_departments": [
        {
            "dept_name": "Sales Department",
            "sales": 200,
            "sub_departments": [
                {
                    "dept_name": "B2B Sales",
                    "sales": 120,
                }
            ]
        },
        {
            "dept_name": "IT Department",
            "sales": 150,
            "sub_departments": [
                {
                    "dept_name": "DevOps",
                    "sales": 300,
                    "sub_departments": [
                        {
                            "dept_name": "Cloud Infrastructure",
                            "sales": 180,
                        }
                    ]
                },
                {
                    "dept_name": "QA Department",
                    "sales": 90,
                }
            ]
        }
    ]
}

Пример вывода:
Общая сумма продаж: 1140
"""

company_structure = {
    "dept_name": "Head Office",
    "sales": 100,
    "sub_departments": [
        {
            "dept_name": "Sales Department",
            "sales": 200,
            "sub_departments": [
                {
                    "dept_name": "B2B Sales",
                    "sales": 120,
                }
            ]
        },
        {
            "dept_name": "IT Department",
            "sales": 150,
            "sub_departments": [
                {
                    "dept_name": "DevOps",
                    "sales": 300,
                    "sub_departments": [
                        {
                            "dept_name": "Cloud Infrastructure",
                            "sales": 180,
                        }
                    ]
                },
                {
                    "dept_name": "QA Department",
                    "sales": 90,
                }
            ]
        }
    ]
}

def summarize_sales(department, sales_name):
    pass

try:
    pass
except ...:
    pass
""" 05 Читабельный формат словаря

Дан вложенный словарь. Напишите рекурсивную функцию, которая
- преобразует его в «плоский» формат,
    где в ключе будет содержаться полный путь к значению.

Данные:
data = {
    "user": {
        "id": 123,
        "info": {
            "name": "Alice",
            "location": {
                "city": "Berlin",
                "coordinates": {"lat": 52.52, "lon": 13.405}
            },
            "hobby": ["swimming", "drawing"]
        }
    },
    "score": 95
}

Пример вывода:
Данные для анализа:
user.id : 123
user.info.name : Alice
user.info.location.city : Berlin
user.info.location.coordinates.lat : 52.52
user.info.location.coordinates.lon : 13.405
user.info.hobby : ['swimming', 'drawing']
score : 95
"""


def parse_data(data, parent_key="", result=None):
    pass


data = {
    "user": {
        "id": 123,
        "info": {
            "name": "Alice",
            "location": {
                "city": "Berlin",
                "coordinates": {"lat": 52.52, "lon": 13.405}
            },
            "hobby": ["swimming", "drawing"]
        }
    },
    "score": 95
}

parsed_data = parse_data(data)
print("Данные для анализа:")
for k, v in parsed_data.items():
    print(k, ":", v)