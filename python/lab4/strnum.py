import re

text = "Python123"

if re.search(r'\d', text):
    print("Number found")
else:
    print("Number not found")