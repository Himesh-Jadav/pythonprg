n = int(input("Enter number of terms: "))

sum = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        sum -= 1 / i
    else:
        sum += 1 / i

print("Sum =", sum)