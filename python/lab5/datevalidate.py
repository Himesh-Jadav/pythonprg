li = ["23-01-2026", "21-13-2026"]
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for i in li:
    d, m, y = map(int, i.split("-"))

    if y % 4 == 0:
        days[1] = 29

    if 1 <= m <= 12 and 1 <= d <= days[m - 1]:
        print("Valid Date")
    else:
        print("Invalid Date")
