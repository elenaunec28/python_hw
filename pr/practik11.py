# Аннотация структур данных
# Напишите функцию, которая принимает список строк и возвращает словарь, где ключи — строки, а значения — длина этих строк. Добавьте документацию и аннотации типов для всех параметров и возвращаемого значения.
#
# Данные:
#words = ["apple", "banana", "cherry"]
# Пример вывода:
# {'apple': 5, 'banana': 6, 'cherry': 6}

#from typing import List, Dict

# def get_words_with_len(words_data: list[str]) -> dict[str, int]:
#     return {word: len(word) for word in words_data}
#
# words = ["apple", "banana", "cherry"]
# print(get_words_with_len(words))


# Генерация отчёта
# Напишите функцию, которая принимает имя пользователя и необязательный список его достижений.
# Если список пуст, возвращается сообщение "Нет достижений".
# Если список не пуст, возвращается строка с перечислением достижений.
# Добавьте документацию и аннотации типов для всех параметров и возвращаемого значения.
#
# Данные:
name = "Alice"
achievements = ["Won chess tournament", "Completed marathon", "Published a book"]
# Пример вывода:
#
# Alice: Won chess tournament, Completed marathon, Published a book
def get_name_achievements(name:str, achievements: list[str] | None = None) -> str:

    if achievements:
        return f"{name} achievements: {', '.join(achievements)}"
    return "No achievements"
print(get_name_achievements(name, achievements))
print(get_name_achievements(name))

# Задание 1.1
# Фильтрация четных с функцией
# Напишите функцию-предикат, которая проверяет четный ли переданный элемент. Также напишите функцию, которая принимает функцию-предикат и список чисел. Она должна возвращать новый список, содержащий только элементы, для которых предикат возвращает True.
# Данные:
nums = [1, 2, 3, 4, 5, 6]
# Пример вывода:
# [2, 4, 6]
def is_even(num: int) -> bool:
    return num % 2 == 0

from typing import Callable

def filter_by(predicate: Callable[[int], bool], nums: list[int]) -> list[int]:
    return [num for num in nums if predicate(num)]

print(filter_by(is_even, nums))
