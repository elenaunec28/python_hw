"""02 Логирование ошибок

Перенаправьте в предыдущей задаче вывод ошибок в файл errors.log
в соответствии с форматом ниже.

ВАЖНО: используйте вывод ошибок
    - и в файл,
    - и на экран.

Пример вывода:
2025-02-23 22:38:53,686 - ERROR - test.py - 16 - Ошибка: Введено некорректное число.

"""

import logging

file_handler = logging.FileHandler("errors.log")
file_handler.setLevel(logging.DEBUG)

stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(filename)s - %(lineno)d - %(message)s"
)
file_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

logging.basicConfig(level=logging.DEBUG, handlers=[file_handler, stream_handler])


def safe_division(dividend, divisor):
    try:
        dividend = float(dividend)
        divisor = float(divisor)
        result = dividend / divisor
        print(f"Результат: {result}")
    except ZeroDivisionError as e:
        logging.error(f"Ошибка: Деление на ноль невозможно: {e}")
    except ValueError as e:
        logging.error(f"Ошибка: Введено некорректное число: {e}")


# Пример вызова функции
safe_division("a", 5)  # False
safe_division(5, 0)  # False
safe_division(5, 2)  # True
safe_division("5.5", "1.2")  # True

# 2025-11-07 11:41:34,147 - ERROR - homework_33_02.py - 48 - Ошибка: Введено некорректное число: could not convert string to float: 'a'
# 2025-11-07 11:41:34,148 - ERROR - homework_33_02.py - 50 - Ошибка: Деление на ноль невозможно: float division by zero
# Результат: 2.5
# Результат: 4.583333333333334
