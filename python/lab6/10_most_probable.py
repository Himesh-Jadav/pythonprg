s = input("Enter a sentence: ")
words = s.split()
count = {}

for word in words:
    count[word] = count.get(word, 0) + 1

print(max(count, key=count.get))