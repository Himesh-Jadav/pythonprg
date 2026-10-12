series = [
    -10 + sum(4*i**2 - 2 for i in range(1, n))
    for n in range(1, 6)
]

print(series)