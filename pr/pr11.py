# Популярные слова
# Реализуйте функцию, которая принимает любое количество строк с текстом.
# Функция должна возвращать подсчет самых популярных слов в количестве, переданном в функцию.
# Программа должна игнорировать регистр слов. Выведите 5 самых популярных слов и их количество.
# Данные:
# text1 = "This is a sample text with some repeated words."
# text2 = "Another sample text with different words."
# text3 = "Text processing is fun when words repeat."
# #
# # Пример вывода:
# # 5 самых популярных слов:
# # words: 3
# # text: 3
# # with: 2
# # sample: 2
# # is: 2
# from collections import Counter
# def popular_words(num, *strings):
#     s = " ".join(strings).replace(".","").lower().split()
#     print(s)
#     count = Counter(s)
#     return count.most_common(num)
#
# print(popular_words(3, text1, text2, text3))

# Группировка задач по категории
# Реализуйте функцию, которая принимает словарь задач с категориями и группирует задачи по их категориям.
# Данные:
# tasks_data = {
# "task1": "работа",
# "task2": "учёба",
# "task3": "развлечения",
# "task4": "работа",
# "task5": "учёба"
# }
# #
# # Пример вывода:
# # Группировка по категориям:
# # {
# # 'работа': ['task1', 'task4'],
# # 'учёба': ['task2', 'task5'],
# # 'развлечения': ['task3']
# # }
#
#
# from collections import defaultdict
# def group_by_category(tasks):
#     group_tasks = defaultdict(list)
#     for task, category in tasks.items():
#         group_tasks[category].append(task)
#     return dict(group_tasks)
# print(group_by_category(tasks_data))


# Поиск задач
# Реализуйте функцию, которая принимает словарь задач с категориями и нужную категорию. Функция должна возвращать список задач для указанной категории.
# Данные:
# # tasks = {
# # "task1": "работа",
# # "task2": "учёба",
# # "task3": "развлечения",
# # "task4": "работа",
# # "task5": "учёба"
# # }
# # category = "учёба"
# #
# # Пример вывода:
# # Задачи для категории 'учёба':
# # ['task2', 'task5']
# from collections import defaultdict
# def group_by_category(tasks):
#     group_tasks = defaultdict(list)
#     for task, category in tasks.items():
#         group_tasks[category].append(task)
#     return dict(group_tasks)
# #print(group_by_category(tasks_data))
#
# def get_by_category(tasks, category):
#     # print(group_by_categories(tasks))
#     return group_by_category(tasks).get(category, [])
#
# print(get_by_category(tasks_data, "работа"))
# print(get_by_category(tasks_data, "наука"))

tasks_data = {
"task1": "работа",
"task2": "учёба",
"task3": "развлечения",
"task4": "работа",
"task5": "учёба"
}
# category = "учёба"
#
# Пример вывода:
# Задачи для категории 'учёба':
# ['task2', 'task5']
from collections import defaultdict
def group_by_category(tasks):
    group_tasks = defaultdict(list)
    for task, category in tasks.items():
        group_tasks[category].append(task)
    return dict(group_tasks)
groups = group_by_category(tasks_data)

def get_by_category(tasks, category):
    # print(group_by_categories(tasks))
    return tasks.get(category, [])

print(get_by_category(tasks_data, "работа"))
print(get_by_category(tasks_data, "наука"))