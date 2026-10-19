# Decode train code
trains = {
    "EXP1030": {
        "name": "Express", "time": "10:30",
        "source": "Ahmedabad", "destination": "Mumbai"
    }
}

code = input("Enter train code: ")
print(trains.get(code, "Invalid code"))
