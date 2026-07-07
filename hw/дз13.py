# Прогрессия увеличения
# Напишите программу, которая создаёт новый кортеж, состоящий из элементов изначального в том же порядке. Добавить в него только элементы, которые больше всех предыдущих значений в исходном кортеже.
# Данные:
#
# numbers = (3, 7, 2, 8, 5, 10, 1)
# # #
# # # Пример вывода:
# # # Кортеж по возрастанию: (3, 7, 8, 10)
# # result = ()
# # max_val = None
# # for num in numbers:
# #     if max_val is None or num > max_val:
# #         result += (num,)
# #         max_val = num
# # print("Кортеж по возрастанию:", result)
# #
#
# result = numbers[:1]
# max_val = numbers[0]
# for num in numbers[1:]:
#     if num > max_val:
#         result += (num,)
#         max_val = num
# print("Кортеж по возрастанию:", result)
#
# Повторяющиеся элементы
# Напишите программу, которая находит индексы элементов кортежа, встречающихся более одного раза.
# Вывести сами элементы и их индексы.
# Данные:
#
numbers = (1, 2, 3, 4, 2, 5, 3, 6, 4, 2, 9)
#
# Пример вывода:
# Индексы элемента 2: 1 4 9
# Индексы элемента 3: 2 6
# Индексы элемента 4: 3 8
index_dict =[]
for index, value in enumerate(numbers):
    if numbers.count(value) > 1 and index not in index_dict:
        print(f"Индексы элемента {value}: ", end="")
        start = index
        while value in numbers[start:]:
            found_index = numbers.index(value, start)
            index_dict += [found_index]
            print(found_index, end=" ")
            start = found_index + 1
        print()



