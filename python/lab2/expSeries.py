import math

x = float(input("Enter x: "))
n = int(input("Enter number of terms: "))

sum = 0

for i in range(n):
    term = (x ** i) / math.factorial(i)
    sum += term

print("e^x =", sum)