s = ["Welcome to NIT Trichy", "Welcome to Facebook", "Welcome to Instagram"]

passwords = {(''.join(i[0] for i in phrase.split())) + "@2006" :phrase for phrase in s}
print(passwords)