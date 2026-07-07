""" 01 Популярные слова
Реализуйте функцию, которая принимает любое количество строк с текстом.
Функция должна возвращать подсчет самых популярных слов в количестве, переданном в функцию. Программа должна игнорировать регистр слов. Выведите 5 самых популярных слов и их количество.
Данные:
text1 = "This is a sample text with some repeated words."
text2 = "Another sample text with different words."
text3 = "Text processing is fun when words repeat."
Пример вывода:
5 самых популярных слов:
	words: 3
	text: 3
	with: 2
	sample: 2
	is: 2
"""

from collections import Counter


def popular_words(count, *texts):
    full_text = " ".join(texts).replace(",", "").replace(".", "").lower()
    words = full_text.split()

    popular = Counter(words).most_common(count)

    print(f"{count} самых популярных слов:")
    for word, cnt in popular:
        print(f"    {word}: {cnt}")

text1 = "This is a sample text with some repeated words."
text2 = "Another sample text with different words."
text3 = "Text processing is fun when words repeat."

popular_words(5, text1, text2, text3)
# 5 самых популярных слов:
# 	text: 3
# 	words: 3
# 	is: 2
# 	sample: 2
# 	with: 2

"""02 Группировка задач по категории
Реализуйте функцию, которая принимает словарь задач с категориями и группирует задачи по их категориям.
Данные:
tasks = {
    "task1": "работа",
    "task2": "учёба",
    "task3": "развлечения",
    "task4": "работа",
    "task5": "учёба"
}
Пример вывода:
Группировка по категориям:
{
    'работа': ['task1', 'task4'],
    'учёба': ['task2', 'task5'],
    'развлечения': ['task3']
}
"""

from collections import defaultdict

def group_tasks_by_category(tasks):
    group = defaultdict(list)

    for task, category in tasks.items():
        group[category].append(task)

    return dict(group)

tasks = {
    "task1": "работа",
    "task2": "учёба",
    "task3": "развлечения",
    "task4": "работа",
    "task5": "учёба"
}

sample = {
    'работа': ['task1', 'task4'],
    'учёба': ['task2', 'task5'],
    'развлечения': ['task3']
}

result = group_tasks_by_category(tasks)
print(result)
print(result == sample)
""" 03 Поиск задач

Реализуйте функцию, которая
- принимает словарь задач с категориями
- и нужную категорию.

Функция должна возвращать список задач для указанной категории.

Данные:
tasks = {
    "task1": "работа",
    "task2": "учёба",
    "task3": "развлечения",
    "task4": "работа",
    "task5": "учёба"
}
category = "учёба"
Пример вывода:
Задачи для категории 'учёба':
['task2', 'task5']
"""

def find_tasks_by_category(tasks, category):
    return [task for task, cat in tasks.items() if cat == category]

tasks = {
    "task1": "работа",
    "task2": "учёба",
    "task3": "развлечения",
    "task4": "работа",
    "task5": "учёба"
}
category = "учёба"
result = find_tasks_by_category(tasks, category)

print(f"Задачи для категории '{category}':")
print(result)


""" 04 Очередь задач с приоритетом
Есть очередь задач, где каждая задача имеет приоритет: "высокий", "средний", "низкий".
Реализуйте функцию, которая сортирует очередь задач таким образом, чтобы более высокий приоритет был в начале очереди.
Нужно изменить исходную очередь, а не создавать новую.
Данные:
tasks = OrderedDict({
    "task1": "низкий",
    "task2": "средний",
    "task3": "высокий",
    "task4": "низкий",
    "task5": "высокий"
})
Пример вывода:
Очередь задач:
	task3: высокий
	task5: высокий
	task2: средний
	task1: низкий
	task4: низкий
"""
from collections import OrderedDict

tasks = OrderedDict({
    "task1": "низкий",
    "task2": "средний",
    "task3": "высокий",
    "task4": "низкий",
    "task5": "высокий"
})

def sort_by_priority(tasks):
    low_priority_keys = [
        key for key, priority in tasks.items() if priority == "низкий"
    ]

    high_priority_keys = [
        key for key, priority in tasks.items() if priority == "высокий"
    ]

    for key in low_priority_keys:
        tasks.move_to_end(key, last=True)

    for key in reversed(high_priority_keys):
        tasks.move_to_end(key, last=False)

sort_by_priority(tasks)

print("Очередь задач:")
for task, priority in tasks.items():
    print(f"    {task}: {priority}")


""" 05 Подсчёт посещений страниц

Реализуйте функцию, которая
- принимает список посещённых страниц
- и подсчитывает количество посещений каждой страницы, используя defaultdict.

Данные:
pages = ["home", "about", "home", "products", "home", "contact", "products"]
Пример вывода:
Посещения страниц:
{'home': 3, 'about': 1, 'products': 2, 'contact': 1}
"""

from collections import defaultdict

def count_page_visits(pages):
    pass

pages = ["home", "about", "home", "products", "home", "contact", "products"]
sample = {'home': 3, 'about': 1, 'products': 2, 'contact': 1}

result = count_page_visits(pages)
print(result)
print(result == sample)

# {'home': 3, 'about': 1, 'products': 2, 'contact': 1}
# True
""" 06 Группировка слов по длине
Реализуйте функцию, которая группирует слова по их длине в и возвращает словарь с ними.
Данные:
words = ["apple", "banana", "kiwi", "grape", "orange", "peach"]

Пример вывода:
Слова по длине:
5: ['apple', 'grape', 'peach']
6: ['banana', 'orange']
4: ['kiwi']
"""

from collections import defaultdict


def group_words_by_length(words):
    pass


words = ["apple", "banana", "kiwi", "grape", "orange", "peach"]
""" 07 Создание глобального счётчика

Создайте функцию increment_counter, которая
- использует глобальную переменную counter для подсчёта вызовов этой функции.

Пример вызова:
increment_counter()
increment_counter()
print(counter)

Пример вывода:
Вызовов функции: 2
"""

counter = 0

def increment_counter():
    pass

increment_counter()
increment_counter()
print("Вызовов функции:", counter)
""" 08 Очередь с LRU-кэшированием

Реализуйте функцию, которая
- поддерживает механизм LRU-кэша для очереди задач.

Функция должна принимать:
Текущую очередь задач.
Новые задачи для добавления.
Максимальный размер очереди.
Если лимит очереди превышен, удаляйте задачи, которые не использовались дольше всех.

Данные:
tasks = ["task1", "task2", "task3", "task4", "task5", "task6"]
new1 = "task4"
new2 = "task1"
new3 = "task7"
new4 = "task2"

Пример вывода:
Очередь из 4 новых задач: ['task4', 'task1', 'task7', 'task2']
"""

from collections import OrderedDict

def lru_cache(queue, limit, *new_tasks):
    pass


tasks = ["task1", "task2", "task3", "task4", "task5", "task6"]
new1 = "task4"
new2 = "task1"
new3 = "task7"
new4 = "task2"

tasks_limit = 4

result = lru_cache(tasks, tasks_limit, new1, new2, new3, new4)
print(f"Очередь из {tasks_limit} новых задач:", result)
