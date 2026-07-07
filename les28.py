# Номер покупки
# Дан список покупок. Найдите какой по счету (начиная с единицы) товар с названием "Milk".
# Если товара нет, выведите сообщение об отсутствии.
#
# Данные:
# products = ["Bread", "Butter", "Cheese", "Milk", "Eggs"]
# Товар "Milk" в списке покупок: 4
products = ["Bread", "Butter", "Cheese", "Milk", "Eggs"]

if 'Milk' in products:
        print(f"Товар 'Milk' в списке покупок: {products.index('Milk') +1 }")
else:
    print("Товара нет в наличии ")
# Список уникальных слов
# Дан текст. Программа должна:
# Разбить текст на слова.
# Создать список уникальных слов в алфавитном порядке (не учитывая регистр).
# Вывести количество уникальных слов.
# Данные:
# text = "Python is a great programming language. Python is popular and powerful."
# Количество уникальных слов: 9
# Уникальные слова: ['a', 'and', 'great', 'is', 'language', 'popular', 'powerful', 'programming', 'python']
text = "Python is a great programming language. Python is popular and powerful."
correct_text = text.lower().replace('.', '')
splited_text = correct_text.split()
uniq_text = list()

for word in splited_text:
    if word not in uniq_text:
        uniq_text.append(word)

print(f"Уникальные слова: {uniq_text}, Количество уникальных слов: {len(uniq_text)} ")
# Перемещение в конец
# Напишите программу, которая перемещает все элементы списка, меньше 5, в конец списка,
# сохраняя порядок остальных элементов.
# Данные:
# numbers = [4, 7, 1, 6, 3, 8, 2]
#
#Перемещённые элементы: [7, 6, 8, 4, 1, 3, 2]
numbers = [4, 7, 1, 6, 3, 8, 2]
# for item in numbers:
#     if item >= 5:
#         new_list.append(item)
#
# for item in numbers:
#     if item < 5:
#         new_list.append(item)
for i, item in enumerate(numbers):
    if item < 5:
        numbers.pop(i)
        numbers.append(item)

print("Перемещённые элементы:", numbers)

# Суммы пар
# Напишите программу, которая обрабатывает список чисел и возвращает новый список,
# содержащий все возможные суммы пар разных элементов без дубликатов значений. Результат должен быть
# отсортирован по убыванию.
# Данные:
# numbers = [3, 5, 9]
# Суммы пар чисел по убыванию: [14, 12, 8]


numbers = [3, 5, 9]
l = []

for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        sum = numbers[i] + numbers[j]
        if sum not in l:
            l.append(sum)

l.sort(reverse=True)
print(l)

# Покупки с лимитом бюджета
# Дан список покупок, где каждый элемент — это кортеж с названием товара и его ценой.
# Покупки распределены по приоритетности. Пользователь вводит бюджет. Программа должна вывести:
# список покупок, которые он может себе позволить;
# итоговую стоимость этих товаров.
# Данные:
# shopping_list = [
# ("Bread", 1.20),
# ("Milk", 0.99),
# ("Eggs", 2.50),
# ("Butter", 3.75),
# ("Cheese", 4.10),
# ("Apple", 0.50)
# ]
# Введите ваш бюджет: 7
#
# Покупки в рамках бюджета:
# Bread: $1.20
# Milk: $0.99
# Eggs: $2.50
# Apple: $0.50
#
# Итоговая стоимость: $5.19
shopping_list = [
 ("Bread", 1.20),
 ("Milk", 0.99),
 ("Eggs", 2.50),
 ("Butter", 3.75),
 ("Cheese", 4.10),
 ("Apple", 0.50)
]

budget = 7
total = 0
print("Покупки в рамках бюджета:")
for item, price in shopping_list:
    if budget >= price:
        budget -= price
        total += price
        print(f"{item}, ${price:.2f}")
print(f"Итоговая стоимость: $ {total:.2f}")


# Оценки студентов
# Дан список студентов, где каждый элемент — это кортеж с именем студента и его оценками. Программа должна вывести их имена и средний балл в виде таблицы. Используйте форматирование для выравнивания колонок.
# Данные:
# students = [
# ("Alice", [85, 90, 78]),
# ("Bob", [88, 76, 92]),
# ("Charlie", [90, 87, 85]),
# ("Diana", [72, 80, 65])
# ]
# Имя       Средний балл
# Alice            84.33
# Bob              85.33
# Charlie          87.33
# Diana            72.33