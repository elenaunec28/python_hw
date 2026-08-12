""" 02 Добавление заметок

Продолжите предыдущую программу:
- создайте таблицу notes с полями: id, title, content
- вставьте одну заметку в таблицу
- выполните commit() после вставки
- выведите все заметки используя в формате dict (а не tuple!)

Пример вывода:

All notes:
{'id': 1, 'title': 'First Note', 'content': 'This is the content of my first note.'}

"""

import mysql.connector
from local_settings import dbconfig_write

db_name = "notes_app_060326_elenaukrainets"

with mysql.connector.connect(**dbconfig_write) as connection:
    with connection.cursor() as cursor:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        cursor.execute(f"USE {db_name}")
        print(f"Database '{db_name}' created or already exists.")

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS notes (
                id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                content TEXT
            )
        """)

        cursor.execute(
            "INSERT INTO notes (title, content) VALUES (%s, %s)",
            ("First Note", "This is the content of my first note.")
        )
        connection.commit()

    with connection.cursor(dictionary=True) as dict_cursor:
        dict_cursor.execute("SELECT * FROM notes")

        print("\nAll notes:")
        for note in dict_cursor.fetchall():
            print(note)

# Database 'notes_app_112226_abcdefg' created or already exists.
#
# All notes:
# {'id': 1, 'title': 'First Note', 'content': 'This is the content of my first note.'}
#
# Process finished with exit code 0
