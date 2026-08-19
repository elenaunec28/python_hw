# Обновление цен товаров
#
# Дан список товаров с ценами. Программа должна применить скидку
# к каждому товару и добавить в список элемент с новой ценой.
# В конце вывести таблицу с новой ценой.
#
# Данные:
#
# products = [["Laptop", 1200], ["Mouse", 25], ["Keyboard", 75], ["Monitor", 200]]
#
#
# Пример вывода:
#
# Введите скидку (в процентах): 17
#
# Товар          Старая цена    Новая цена
#
# Laptop            1200.00$       996.00$
#
# Mouse                25.00$         20.75$
#
# Keyboard           75.00$         62.25$
#
# Monitor            200.00$       166.00$
#

products = [["Laptop", 1200], ["Mouse", 25], ["Keyboard", 75], ["Monitor", 200]]

NAME, PRICE = 15, 15

percent = float(input("Введите скидку (в процентах): "))

for product in products:
    product.append(product[1] * (1 - percent / 100))

print(f"{'Товар':<{NAME}}{'Старая цена':>{PRICE}}{'Новая цена':>{PRICE}}\n")

for product, price, nprice in products:
    print(f"{product:<{NAME}}{f'{price:.2f}$':>{PRICE}}{f'{nprice:.2f}$':>{PRICE}}\n")
