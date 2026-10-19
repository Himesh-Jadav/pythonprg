import math

x = float(input("Enter x in radians: "))
n = int(input("Enter number of terms: "))

sum = 0

for i in range(n):
    power = 2 * i
    term = ((-1) ** i) * (x ** power) / math.factorial(power)
    sum += term

print("cos(x) =", sum)