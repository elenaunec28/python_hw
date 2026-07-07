# Напишите программу, которая обрабатывает строку и заменяет все вхождения
# чисел в строке на их квадрат, оставляя другие части строки неизменными.
# Данные:
# text = "I have '2' apples and '14' bananas"
# # Пример вывода:
# # I have 4 apples and 16 bananas
# # new_list = text.split()
# # for i in range(len(new_list)):
# #
# #     if new_list[i].isdigit():
# #         new_list[i] = str(int(new_list[i]) ** 2)
# # print(' '.join(new_list))
# new_list = text.split()
# for i in range(len(new_list)):
#     tmp = new_list[i].strip('\'"')
#     if tmp.isdigit():
#         new_list[i] = "'" + str(int(tmp) ** 2) + "'"
#
# print(' '.join(new_list))
# #f"\"{int(elements[i]) ** 2}\

# Сложение чисел
# Напишите программу, которая принимает строку с числами через пробел и выводит сумму всех чисел.
#
# Пример вывода:
# Введите список чисел через пробел: 1 2 3 4 5
# Сумма чисел: 15
# nums =(input("Введите список чисел через пробел: ")).split()
# summa = 0
# #print(nums)
# for num in nums:
#     summa += int(num)
#     print (summa)


# Максимальное число
# Напишите программу, которая выводит наибольшее число в списке, не используя
# встроенную функцию max(), а также его индекс в списке.
# numbers = [3, 12, 8, 22, 9, 25, 6, 23, 8, 7]
#
# Пример вывода:
# Список чисел: [3, 12, 8, 22, 9, 25, 6, 23, 8, 7]
# Наибольшее число: 25
# Индекс числа: 5
# numbers = [3, 12, 8, 22, 9, 25, 6, 23, 8, 7]
# val = numbers[0]
# index = 0
# for n in range(len(numbers)):
#     if numbers[n] > val:
#         val = numbers[n]
#         index = n
#     print('Наибольшее число:',val)
#     print('Индекс числа:', index)


# Перестановка соседних элементов
# Напишите программу, которая меняет местами соседние элементы списка.
# Пример списка: umbers = [1, 2, 3, 4, 5]
#
# Пример вывода:
# Изначальный список: [1, 2, 3, 4, 5]
# Список после перестановки: [2, 1, 4, 3, 5]
# list1 = [1, 2, 3, 4, 5]
# for i in range(0, len(list1)-1,2):
#     (list1[i], list1[i + 1]) = list1[i + 1], list1[i]
#     #print(list1[i], list1[i+1])
# print(f"Список после перестановки:{list1}")
# Кодирование строки
# Напишите программу, которая принимает строку и кодирует её с помощью следующего правила:
# каждая последовательность одинаковых символов заменяется на символ и количество его повторений. Например, строка aaaabbc превращается в a4b2c1.
#
# Пример вывода:
# Введите строку: aaaabbc
# Закодированная строка: a4b2c1
# s = input("Введите строку: ")
# result = ""
# count = 1
# letter = s[0]
# for i in range(1, len(s)):
#     if letter == s[i]:
#         count += 1
#     else:
#         result += letter
#         letter = s[i]
#         count = 1
#
#
#
# s = input("введите строку")
#
# result =""
# count = 1
# letter = s[0]
# for i in range(1, len(s)):
#     if letter == s[i]:
#         count += 1
#     else:
#         result += letter + str(count)
#         letter = s[i]
#         count = 1
# result += letter + str(count)
# print(result)


# 10. Развернуть слова
# Напишите программу, которая разворачивает каждое слово в строке, сохраняя их порядок.
#
# Пример вывода:
# Введите строку: Python is fun
# Результат: nohtyP si nuf

# Напишите программу, которая проверяет, начинается ли строка с буквы,
# содержит ли в себе символ @, и заканчивается ли на .com или .de.
# Пример вывода: Введите email: user@example.com Корректный формат? True

# Звёздочки вместо чисел
#
# Напишите программу, которая заменяет все цифры в строке на звёздочки *.
#
# text = "My number is 123-456-789"
#
# Пример вывода:
#
# Строка: My number is 123-456-789
#
# Результат: My number is ***-***-***
# text = "My number is 123-456-789"
# result = ""
# for char in text:
#     if char.isdigit():
#         result += "*"
#     else:
#         result += char
# print(text)
# print(result)
#
# text = "My number is 123-456-789"
# for i in "0123456789":
#     text = text.replace(i, "*")
# print(text)

# print(result)
# for char in text:
#     if (ord(char) >= 48) and (ord(char) <= 57):
#         char = '*'
#     text_without_numbers += char
# Количество символов
#
# Напишите программу, которая подсчитывает количество вхождений всех символов в строке. Нужно вывести только символы, которые
# встречаются более 1 раза (игнорируя регистр), с указанием их количества. Выводите повторяющиеся символы только один раз.
# text = "Programming in python"
# Пример вывода:
# Строка: Programming in python
# Символ 'p' встречается 2 раз(а)
# Символ 'r' встречается 2 раз(а)
# Символ 'o' встречается 2 раз(а)
# Символ 'g' встречается 2 раз(а)
# Символ 'm' встречается 2 раз(а)
# Символ 'i' встречается 2 раз(а)
# Символ 'n' встречается 3 раз(а)
# Символ ' ' встречается 2 раз(а)
# text = "Programming in python"
# new_text = text.lower()
# repeat_text = ""
# count = 0
#
# for char in new_text:
#     if char in new_text:
#     count += 1
#     if count > 1:
#     print
#
#
# text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."
#
# result = ""
# num = ""
# i = 0
#
# while i < len(text):
#     ch = text[i]
#
#     if ch.isdigit() or (ch == "." and num):
#         num += ch
#     else:
#         if num:
#             if result.endswith("...."):
#                 result += num
#             else:
#                 result += str(float(num) * 10)
#             num = ""
#         result += ch
#     i += 1
#
# if num:
#     if result.endswith("...."):
#         result += num
#     else:
#         result += str(float(num) * 10)
#
# print(result)
#
#
# flFind = True
# not_find = False
# arbitrary_string = input("Введите email: ") # murzik_ystal@gmail.com
# print(
#         f"{arbitrary_string} Корректный формат? {flFind}"
#         if arbitrary_string[0].isalpha() and "@" in arbitrary_string and (arbitrary_string.endswith(".com") or arbitrary_string.endswith(".de"))
#         else f"{arbitrary_string} Корректный формат? {not_find}"
#       )
# text = input("Введите email: ")
#
# print(text[0].isalpha and "@" in text and text.endswith(".com") or text.endswith(".de"))
#
# text = "user@example.com"
# result = text[0].isalpha() and "@" in text and (".com" in text or ".de" in text)
# print(result)
# text = "user@example.com"
# print(text[0].isalpha() and "@" in text and (text.endswith(".com") or text.endswith(".de")))
text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."
words = text.split()

for i in range(len(words)):
    if words[i].count(".") < 2 and words[i].replace(".", "").isdecimal():
        words[i] = str(float(words[i]) * 10)
new_text = " ".join(words)
print(new_text)


