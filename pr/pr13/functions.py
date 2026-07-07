def read_file(file_name, encoding="utf-8")-> list[dict]:
    sales = []
    with open(file_name, "r", encoding="utf-8") as f:
        for line in f:
            name, date, amount, category, city = line.split(",")
            year = date[:4]
            month = date[5:7]

            sales.append({
                "name": name,
                "date": date,
                "amount": amount,
                "category": category,
                "city": city,
                "year": year,
                "month": month
            })
    return sales

# if __name__ == "__main__":
from pprint import pprint
pprint(read_file("sales_data.txt"))
from collections import defaultdict

def group_sales(sales: list[dict]) -> tuple[dict, dict]:
    grouped_sales = defaultdict(list)
    category_totals = defaultdict(lambda: defaultdict(int))

    for sale in sales:
        year = sale["year"]
        month = sale["month"]
        category = sale["category"]

        grouped_sales[(year, month, category)].append({
            "date": sale["date"],
            "name": sale["name"],
            "amount": sale["amount"],
        })
        category_totals[(year, month)][category] += int(sale["amount"])

    return grouped_sales, category_totals
pprint(group_sales(read_file("sales_data.txt")))