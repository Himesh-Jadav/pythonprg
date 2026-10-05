import re
n=input("enter time  ")
pattern=r"[1-9]|1[1-2]:[1-5][0-9]:[1-5][0-9](a.m|p.m)"
match=re.match(pattern,n)
print(match)