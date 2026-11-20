"""Створює тестовий файл sample_data.csv (запускати за потреби)."""
import random
from datetime import date, timedelta

import pandas as pd

random.seed(7)
items = {
    "Їжа": ("Продукти", 150, 900), "Транспорт": ("Проїзд", 30, 400),
    "Житло": ("Комунальні послуги", 1500, 3500), "Розваги": ("Кіно / кафе", 100, 1200),
    "Здоров'я": ("Аптека", 80, 900), "Одяг": ("Одяг", 400, 2500),
    "Навчання": ("Курси", 300, 2000),
}
rows = []
day = date(2026, 6, 1)
while day <= date(2026, 11, 10):
    for _ in range(random.choice([0, 1, 1, 2])):
        cat = random.choices(list(items), weights=[6, 4, 1, 3, 2, 1, 1])[0]
        desc, lo, hi = items[cat]
        rows.append({"date": day.isoformat(), "category": cat, "description": desc,
                     "amount": round(random.uniform(lo, hi), 2)})
    day += timedelta(days=1)
pd.DataFrame(rows).to_csv("sample_data.csv", index=False, encoding="utf-8-sig")
print("Записів:", len(rows))
