"""
Конвертация времени

Найдите сколько недель, дней, часов, минут, секунд содержится в ста миллионах секунд.

Пример:
Enter the number of seconds: 150 100 100

weeks: 165
days: 2
hours: 9
minutes: 46
seconds: 40
"""
SEC_IN_MINUTE = 60
SEC_IN_HOUR = 60 * SEC_IN_MINUTE
SEC_IN_DAY = 24 * SEC_IN_HOUR
SEC_IN_WEEK = 7 * SEC_IN_DAY

# total_seconds = int(input("Enter the number of seconds:"))
total_seconds = 100_000_000

weeks = total_seconds // SEC_IN_WEEK
rest_seconds = total_seconds % SEC_IN_WEEK

days = rest_seconds // SEC_IN_DAY
rest_seconds = rest_seconds % SEC_IN_DAY

hours = rest_seconds // SEC_IN_HOUR
rest_seconds = rest_seconds % SEC_IN_HOUR

minutes = rest_seconds // SEC_IN_MINUTE
seconds = rest_seconds % SEC_IN_MINUTE

print('weeks:', weeks)
print('days:', days)
print('hours:', hours)
print('minutes:', minutes)
print('seconds:', seconds)

"""
Рассчитайте бонус продавцу:
Если sales ≥ 100000, бонус = 10% от продаж.
Иначе бонус = 5% от продаж.
Если клиент VIP-клиент (is_vip == True), то бонус дополнительно увеличивается на 50% (бонус умножается на 1,5)

Требование:
Решить задачу без использования условных операторов.
При выводе результата отбросьте дробную часть.

==============================================================
Пример:
is_vip = True
sales_amount = 100 000

Bonus amount: 15000
"""
THRESHOLD = 100_000
BONUS_HIGH = 0.10
BONUS_LOW = 0.05

sales_amount = 100_000
# sales_amount = int(input("Enter the sales amount:"))
is_vip = True
# is_vip = input("Is VIP (0 - no, 1 - yes): ") == "1"
# is_vip = bool(int(input("Is VIP (0 - no, 1 - yes): ")))

bonus_rate = ((sales_amount >= THRESHOLD ) * BONUS_HIGH
+ (sales_amount < THRESHOLD) * BONUS_LOW)

bonus_rate *= 1 + 0.5 * is_vip
bonus_amount = int(bonus_rate * sales_amount)
print("Bonus amount: ", bonus_amount)