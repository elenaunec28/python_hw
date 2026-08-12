""" 01 Список всех стран

Используя базу данных world, вывести названия всех стран из таблицы country.
Каждое название должно отображаться с новой строки и иметь номер.
Пример вывода:
1. Aruba
2. Afghanistan
3. Angola
...
239. Zimbabwe

Попробуйте решить задачи используя стиль Data Access Object (DAO).
"""

import mysql.connector
from local_settings import dbconfig


class DatabaseError(Exception):
    """Общее исключение слоя доступа к данным"""


class MySQLConnection:
    def __init__(self, dbconfig):
        self.dbconfig = dbconfig
        self.connection = None
        self.cursor = None

    def __enter__(self):
        try:
            self.connection = mysql.connector.connect(**self.dbconfig)
            self.cursor = self.connection.cursor()

        except mysql.connector.Error as e:
            raise DatabaseError(f"Не удалось подключиться к базе данных: {e}") from e

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.cursor:
            self.cursor.close()

        if self.connection:
            self.connection.close()

        return False

class WorldDB(MySQLConnection):
    def fetch_countries(self):
        """Получить список всех стран"""
        try:
            self.cursor.execute("SELECT Name FROM country ;")
            rows = self.cursor.fetchall()

        except mysql.connector.Error as e:
            raise DatabaseError(f"Ошибка выполнения запроса: {e}")

        return [row[0] for row in rows]


if __name__ == "__main__":
    try:
        with WorldDB(dbconfig) as db:
            countries = db.fetch_countries()
            for i, name in enumerate(countries, start=1):
                print(f"{i}. {name}")
    except DatabaseError as e:
        print(f"❌ {e}")
