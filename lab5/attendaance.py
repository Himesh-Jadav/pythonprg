li = ["01-09-2026", 5, 10, 31, 105, "02-12-2026", 2, 5, 10, 35, 102]
present_count = {}
i = 0
while i < len(li):
    if isinstance(li[i], str):
        date = li[i]
        count = 0
        i += 1
        while i < len(li) and not isinstance(li[i], str):
            count += 1
            i += 1
        present_count[date] = count
    else:
        i += 1
for date, count in present_count.items():
    print(f"{date}: {count} present(s)")