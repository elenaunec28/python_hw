""" 02 Города выбранной страны

Добавьте к предыдущей программе возможность выбора страны.
Пользователь должен ввести название страны.
Далее выведите все города этой страны и их численность населения.

Пример вывода 1:
Введите страну: Germany
Berlin — 3386667
Hamburg — 1704735
Munich [München] — 1194560

Пример вывода 2:
Введите страну: Unknown
❌ Страна 'Unknown' не найдена
...

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
            self.cursor = self.connection.cursor(dictionary=True)

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

        return [row["Name"] for row in rows]


    def fetch_cities_by_country(self, country_name):
        """Получить все города выбранной страны с их населением"""
        try:
            query = """ 
                SELECT city.Name, city.Population, city.District 
                FROM city 
                JOIN country ON city.CountryCode = country.Code 
                WHERE country.Name = %s 
                ORDER BY city.Population DESC; 
                """
            self.cursor.execute(query, (country_name,))
            rows = self.cursor.fetchall()
        except mysql.connector.Error as e:
            raise DatabaseError(f"Ошибка выполнения запроса: {e}") from e

        return rows

if __name__ == "__main__":
    try:
        with WorldDB(dbconfig) as db:
            # Список всех стран
            countries = db.fetch_countries()
            print("Список стран:")
            for i, name in enumerate(countries, start=1):
                print(f"{i}. {name}")

            # Ввод страны пользователем
            country_input = input("\nВведите страну: ").strip()

            # Получаем города выбранной страны
            cities = db.fetch_cities_by_country(country_input)
            if not cities:
                print(f"Для страны '{country_input}' нет данных о городах.")
            else:
                for city in cities:
                    # Формируем строку с названием города и населением
                    city_name = city['Name']
                    district = city['District']
                    population = city['Population']
                    # Если нужно — можно добавить район/альтернативное имя
                    print(f"{city_name} — {population}")

    except DatabaseError as e:
        print(f"❌ {e}")
