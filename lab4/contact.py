import re
n=input(" enter phone number : ")
pattern=r"\d{2}-\d{2}-\d+"
match=re.match(pattern,n)
print(match)