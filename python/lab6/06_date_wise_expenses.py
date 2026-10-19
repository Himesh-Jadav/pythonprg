# Total expenses date-wise
expenses = [
    ("01-10-2026", 500),
    ("01-10-2026", 300),
    ("02-10-2026", 700)
]

daily = {}
for date, amount in expenses:
    daily[date] = daily.get(date, 0) + amount

print(daily)
