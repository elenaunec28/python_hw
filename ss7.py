# Разворот списка
numbers = [3, 1, 4, 1, 5]
reversed_numbers = reversed(numbers)  # возвращает не list, а list_reverseiterator
print(type(reversed_numbers))
print(reversed_numbers)
# list_reversed_numbers = list(reversed_numbers)
# # чтобы увидеть элементы, нужно преобразовать в list
# print(list_reversed_numbers)
# for el in reversed_numbers:
#     print(el)

for _ in range(2):
    print(reversed_numbers.__next__())
print()

list_reversed_numbers = list(reversed_numbers)
# чтобы увидеть элементы, нужно преобразовать в list
print(list_reversed_numbers)


# Напишите программу, которая принимает список строк и создает новый список только из слов,
# начинающихся и заканчиваются одной и той же буквой.
#
# Данные:
# strings = ["apple", "banana", "level", "radar", "grape"]
#
# Пример вывода:
# Строки, которые начинаются и заканчиваются одной и той же буквой: ['level', 'radar']

strings = ["apple", "banana", "level", "radar", "grape"]
new_strings = []

for s in strings:
    if s[0] == s[-1]:
        new_strings.append(s)
print(new_strings)