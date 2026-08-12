""" 01 Добавление товаров

Создайте программу, которая подключается к MongoDB и:
- выбирает базу ich_edit и коллекцию products_<your_group>_<your_full_name>
- очищает коллекцию перед началом
- добавляет 3 товара с полями: name, price, stock
- выводит сообщение о количестве добавленных товаров
Пример вывода:
3 products inserted.
"""


from pymongo import MongoClient
from local_settings import MONGODB_URL_WRITE

products = [
    {"name": "Laptop", "price": 1200, "stock": 5},
    {"name": "Mouse", "price": 25, "stock": 50},
    {"name": "Keyboard", "price": 70, "stock": 20}
]

collection_name = "products_060326_elena"

with MongoClient(MONGODB_URL_WRITE) as client:
    db = client["ich_edit"]
    collection = db[collection_name]

    collection.delete_many({})

    result = collection.insert_many(products)

    print(f"{len(result.inserted_ids)} products inserted.")

# 3 products inserted.
