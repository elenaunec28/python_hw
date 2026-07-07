""" 01 Номер покупки

Дан список покупок.
Найдите какой по счету (начиная с единицы) товар с названием "Milk".
Если товара нет, выведите сообщение об отсутствии.

Данные:
products = ["Bread", "Butter", "Cheese", "Milk", "Eggs"]

Пример вывода:
Товар "Milk" в списке покупок: 4
"""
from idlelib.replace import replace

from les28 import uniq_text

products = ["Bread", "Butter", "Cheese", "Milk", "Eggs"]
item = "Milk"
if item not in products:
    print(f'Товар "{item}" отсутствует')
else:
    print(f'Товар "{item}" в списке покупок: {products.index(item) + 1}')



""" 02 Список уникальных слов

Дан текст. Программа должна:
Разбить текст на слова.
Создать список уникальных слов в алфавитном порядке (не учитывая регистр).
Вывести количество уникальных слов.

Данные:
text = "Python is a great programming language. Python is popular and powerful."

Пример вывода:
Количество уникальных слов: 9
Уникальные слова: ['a', 'and', 'great', 'is', 'language', 'popular', 'powerful', 'programming', 'python']
"""

text = "Python is a great programming language. Python is popular and powerful."
format_text = text.replace(".", "").lower().split()
uniq_text = []
for word in format_text:
    if word not in uniq_text:
        uniq_text.append(word)
uniq_text.sort()
print("Количество уникальных слов:", len(uniq_text))
print("Уникальные слова:", uniq_text)


""" 03 Самое длинное слово
Дано предложение.
Найдите самое длинное слово
и выведите это слово с его длиной.

Данные:
sentence = "Programming in Python is both fun and educational"

Пример вывода:
Самое длинное слово: Programming
Длина слова: 11
"""

sentence = "Programming in Python is both fun and educational"
max_word = max(sentence.split(), key=len)
print("Самое длинное слово:", max_word)
print("Длина слова:", len(max_word))


""" 04 Перемещение в конец

Напишите программу, которая модифицирует текущий список,
    перемещая все элементы меньше 5, в конец списка,
    но сохраняя при этом порядок остальных элементов.

ВАЖНО: НЕ создаём новый список, а модифицируем уже существующий!

Данные:
numbers = [4, 3, 7, 1, 2, 6, 3, 4, 8, 2]

Пример вывода:
Перемещённые элементы: [7, 6, 8, 4, 3, 1, 2, 3, 4, 2]
"""

numbers = [4, 3, 7, 1, 2, 6, 3, 4, 8, 2]

FLAG = 5
numbers = [4, 3, 7, 1, 2, 6, 3, 4, 8, 2]
# numbers = [4, 3, 7]
l = len(numbers)
idx_for_del = []

print(id(numbers))
for i in range(l):
    if numbers[i] < FLAG:
        numbers.append(numbers[i])
        idx_for_del.append(i)

for i in reversed(idx_for_del):
    del numbers[i]

print(id(numbers))
print("Перемещённые элементы:", numbers)




""" 05 Суммы пар

Напишите программу, которая
- обрабатывает список чисел
- и возвращает новый список,
        содержащий все возможные суммы пар разных элементов без дубликатов значений.
- Результат должен быть отсортирован по убыванию.

Данные:
numbers = [3, 5, 9]

Пример вывода:
Суммы пар чисел по убыванию: [14, 12, 8]
"""

numbers = [3, 5, 9]


# """ 06 Покупки с лимитом бюджета
#
# Дан список покупок, где каждый элемент — это тюпл: (товар, цена).
# Покупки распределены по приоритетности.
# Пользователь вводит бюджет.
# Программа должна вывести:
# - список покупок, которые он может себе позволить;
# - итоговую стоимость этих товаров.
#
# Данные:
# shopping_list = [
#     ("Bread", 1.20),
#     ("Milk", 0.99),
#     ("Eggs", 2.50),
#     ("Butter", 3.75),
#     ("Cheese", 4.10),
#     ("Apple", 0.50)
# ]
#
# Пример вывода:
# Введите ваш бюджет: 7
#
# Покупки в рамках бюджета:
# Bread: $1.20
# Milk: $0.99
# Eggs: $2.50
# Apple: $0.50
#
# Итоговая стоимость: $5.19
# """
#
# shopping_list = [
#     ("Bread", 1.20),
#     ("Milk", 0.99),
#     ("Eggs", 2.50),
#     ("Butter", 3.75),
#     ("Cheese", 4.10),
#     ("Apple", 0.50)
# ]
#
# budget = 7  # int(input("Введите ваш бюджет: "))