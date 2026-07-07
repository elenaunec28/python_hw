text = input("Введите зашифрованный текст: ")
shift = int(input("Введите сдвиг: "))
i = 0
decrypt = ""

while i < len(text):
    char = text[i]
    i += 1
    decrypt += chr(ord(char) - shift)
print(decrypt)
result = 1
while True:
    user_input = input("Введите число для перемножения: ")
    if user_input == "0":
        print("Пропуск итерации")
        continue # Пропускаем оставшуюся часть текущей итерации
    if user_input == "exit":
        print("Выход из программы")
        break # Прерывание цикла
    result *= int(user_input)
    print("Результат перемножения:", result)
i = 1
while i <= 3:
    if i == 2:
        i += 1
    continue
    print(i)
    i += 1
else:
    print("Цикл завершён.")
