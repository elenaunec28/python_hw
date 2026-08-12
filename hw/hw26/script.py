#     Поиск и удаление файлов с указанным расширением
#
# Напишите программу, которая:
#
#     Принимает путь к директории и расширение файлов через аргумент командной строки.
#
#     Рекурсивно ищет файлы с этим расширением во всех вложенных папках.
#
#     Спрашивает у пользователя, хочет ли он удалить найденные файлы.
#
#     Если пользователь подтверждает, удаляет их.
#
# Пример запуска:
#
# python 1.py /home/user/PycharmProjects/project1 .log
#
# Пример вывода
#
# Найдены файлы с расширением '.log':
#
# - logs/error.log
#
# - logs/system.log
#
# - logs/backup/old.log
#
# - logs/backup/debug.log
#
# Вы хотите удалить эти файлы? (y/n): y
#
# Удаление завершено.

""" 02 Поиск и удаление файлов с указанным расширением """

import sys
import os

directory = sys.argv[1]
extension = sys.argv[2]

found_files = []

print(f"Найдены файлы с расширением '{extension}':")
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(extension):
            path = os.path.join(root, file)
            found_files.append(path)
            print(f"- {path}")

if found_files:
    answer = input("Вы хотите удалить эти файлы? (y/n): ")
    if answer == "y":
        for file in found_files:
            os.remove(file)
        print("Удаление завершено.")
else:
    print("Файлы не найдены.")