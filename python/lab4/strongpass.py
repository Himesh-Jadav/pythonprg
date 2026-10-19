import re
n=input("enter your password")
pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9])(?=.*[0-9]).{8,}$"
match=re.match(pattern,n)
if(match and len(n)>=8):
    print(" it's a strong password ")
else:
    print("no")