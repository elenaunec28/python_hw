#     Список файлов и папок
#
# Напишите программу, которая принимает путь к директории через аргумент командной строки и выводит:
#
#     Отдельно список папок
#
#     Отдельно список файлов
#
# Пример запуска
#
# python 1.py /home/user/documents
#
# Пример вывода
#
# Содержимое директории '/home/user/documents':
#
# Папки:
#
# - folder1
#
# - folder2
#
# Файлы:
#
# - file1.txt
#
# - file2.txt
#
# - notes.docx
""" 01 Список файлов и папок """

import sys
import os


def list_directory_contents(path: str) -> None:
    if not os.path.isdir(path):
        print(f"Ошибка: '{path}' не является директорией или не существует.")
        return

    entries = os.listdir(path)

    folders = [entry for entry in entries if os.path.isdir(os.path.join(path, entry))]
    files = [entry for entry in entries if os.path.isfile(os.path.join(path, entry))]

    print(f"Содержимое директории '{path}':")

    print("\nПапки:")
    for folder in sorted(folders):
        print(f"- {folder}")

    print("\nФайлы:")
    for file in sorted(files):
        print(f"- {file}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python 1.py <путь_к_директории>")
        sys.exit(1)

    directory_path = sys.argv[1]
    list_directory_contents(directory_path)