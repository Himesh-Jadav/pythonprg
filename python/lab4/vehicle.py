import re
n=input(" enter vehicle no :")
pattern=r"[A-Z]{2}[0-9][0-9][A-Z]{2}[0-9]{4}"
match=re.match(pattern,n)
print(match)