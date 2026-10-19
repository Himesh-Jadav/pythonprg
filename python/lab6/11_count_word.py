doc = input("Enter document: ")
word = input("Enter word: ")

words = doc.split()
print("Count:", words.count(word))