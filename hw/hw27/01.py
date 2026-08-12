""" 01 Фильтрация по ключевому слову

Напишите программу, которая
- ищет в файле все строки, содержащие указанное пользователем слово,
- и сохраняет их в новый файл.

Имя нового файла формируется как <keyword>_<original_filename>.
Если файл не существует, программа должна вывести ошибку.
Если совпадения не найдены, новый файл не создаётся.

Используйте файл system_log.txt.

Пример ввода:
Введите имя файла для поиска: system_log.txt
Введите ключевое слово: error

Пример вывода:
Строки, содержащие 'error', сохранены в <keyword>_<original_filename>.

"""

def find_keyword(filename: str, keyword: str) -> None:
    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError as e:
        print(f"File not found: {e}")
        return

    matched_lines = [line for line in lines if keyword in line]

    if not matched_lines:
        return

    new_filename = f"{keyword}_{filename}"
    with open(new_filename, "w", encoding="utf-8") as f:
        f.writelines(matched_lines)

    print(f"Строки, содержащие '{keyword}', сохранены в {new_filename}.")


find_keyword('s', 'error')
# File not found: [Errno 2] No such file or directory: 's'

find_keyword('system_log.txt', 'error')
# Строки, содержащие 'error', сохранены в error_system_log.txt.

