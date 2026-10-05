import re

text = "Python"

if re.fullmatch(r'[A-Za-z]+', text):
    print("Only alphabets")
else:
    print("Contains other characters")