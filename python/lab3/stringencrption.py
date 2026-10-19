text = input("Enter a string: ")
encrypted = ""
for i in range(len(text)):
    if i % 2 == 0:
        encrypted += chr(ord(text[i]) + 1)
    else:
        encrypted += chr(ord(text[i]) - 1)
print("Encrypted string:", encrypted)

decrypted = ""
for i in range(len(encrypted)):
    if i % 2 == 0:
        decrypted += chr(ord(encrypted[i]) - 1)
    else:
        decrypted += chr(ord(encrypted[i]) + 1)

print("Decrypted string:", decrypted)
