import re

pin = input("Enter PIN code: ")

if re.fullmatch(r'[1-9]\d{5}', pin):
    print("Valid PIN")
else:
    print("Invalid PIN")