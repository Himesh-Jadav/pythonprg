from datetime import date

dob = {
    'Himesh': '26-07-2006',
    'Hatim': '25-10-2004',
    'Kabir': '06-09-2005'
}

Age = {}

today = date.today()
c_day = today.day
c_month = today.month
c_year = today.year

for name, dob_str in dob.items():
    day, month, year = map(int, dob_str.split('-'))

    current_age = c_year - year

    # Birthday has not occurred yet this year
    if (c_month, c_day) < (month, day):
        current_age -= 1

    Age[name] = current_age

print(Age)