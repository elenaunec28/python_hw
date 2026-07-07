# Звёздочки вместо чисел
# Напишите программу, которая заменяет все цифры в строке на звёздочки *.
# text = "My number is 123-456-789"
# Пример вывода:
# Строка: My number is 123-456-789
# Результат: My number is ***-***-***
text = "My number is 123-456-789"
result = ""
for char in text:
    if char.isdigit():
        result += "*"
    else:
        result += char
print(text)
print(result)


text = "My number is 123-456-789"
for i in "0123456789":
    text = text.replace(i, "*")
print(text)

# Количество символов
# Напишите программу, которая подсчитывает количество вхождений всех символов в строке. Нужно вывести только символы,
# которые встречаются более 1 раза (игнорируя регистр), с указанием их количества. Выводите повторяющиеся символы
# только один раз.
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
text = "Programming in python"
print("Строка: ", text)
text = text.lower()
new_text = ""
count = 0

for char in text:
    if char not in new_text:
        new_text += char
        count = text.count(char)
        if count > 1:
            print("Символ", "'" + char + "'", "встречается", count, "раз(а)")

# Увеличение чисел
# Напишите программу, которая заменяет все числа в строке на их эквивалент, умноженный на 10.
# text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."
# Пример вывода:
# I have 50.0 apples and 100.0 oranges, price is 5.0 each. Card number is ....3672.
text = "I have 5 apples and 10 oranges, price is 0.5 each. Card number is ....3672."
words = text.split()

for i in range(len(words)):
    if words[i].count(".") < 2 and words[i].replace(".", "").isdecimal():
        words[i] = str(float(words[i]) * 10)
new_text = " ".join(words)
print(new_text)