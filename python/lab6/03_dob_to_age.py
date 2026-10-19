# Convert DOB to age
from datetime import date, datetime

people = {"Amit": "15-05-2005", "Rahul": "20-08-2004"}
ages = {}

for name, dob in people.items():
    b = datetime.strptime(dob, "%d-%m-%Y").date()
    age = date.today().year - b.year
    if (date.today().month, date.today().day) < (b.month, b.day):
        age -= 1
    ages[name] = age

print(ages)
