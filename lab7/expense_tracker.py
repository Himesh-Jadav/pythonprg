li = ["2026-10-01", 100, 200, 50,
      "2026-10-02", 300, 150,
      "2026-10-01", 250]

totals = {}
current_date = None

for item in li:
    if isinstance(item, str):
        current_date = item
        totals.setdefault(current_date, 0)
    else:
        totals[current_date] += item

print(totals)