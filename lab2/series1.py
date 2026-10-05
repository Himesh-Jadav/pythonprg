x = float(input("Enter x: "))
n = int(input("Enter number of terms: "))

sum = 0

for i in range(n + 1):
    sum += x ** i

print("Sum =", sum)