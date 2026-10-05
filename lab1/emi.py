p = float(input("Enter loan amount: "))
r = float(input("Enter annual interest rate (%): "))
n = int(input("Enter loan period (in months): "))

r = r / (12 * 100)

emi = (p * r * (1 + r) ** n) / ((1 + r) ** n - 1)

print("Monthly EMI =", round(emi, 2))