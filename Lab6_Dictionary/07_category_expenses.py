# Expenses date-wise and category-wise
expenses = [
    ("01-10-2026", "Food", 200),
    ("01-10-2026", "Travel", 100),
    ("01-10-2026", "Food", 300)
]

result = {}
for date, category, amount in expenses:
    result.setdefault(date, {})
    result[date][category] = result[date].get(category, 0) + amount

print(result)
