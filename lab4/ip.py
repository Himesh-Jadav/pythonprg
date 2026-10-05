import re

s = input("Enter text: ")

ip = re.findall(r'\b(?:\d{1,3}\.){3}\d{1,3}\b', s)

print("IP Addresses:", ip)