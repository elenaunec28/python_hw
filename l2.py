# print('1', '2', '3', '4', '5', sep='---')
# print("\tПервая строка с табуляцией \nВторая строка на новой строке")
print('Это файл "example.txt"')
print("Это файл \"example.txt\" ")
print('''Это файл "example.txt"''')
usr_in = int(input("Введите четырехзначное число:"))
first_num = usr_in // 1000
last_num = usr_in % 10
middle_num = usr_in % 1000//10
result = last_num * 1000 + middle_num * 10 + first_num
print(result)