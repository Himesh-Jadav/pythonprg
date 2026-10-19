s = input("Enter sentence: ")

words = {word: word[:len(word)//2][::-1] + word[len(word)//2:][::-1] for word in s.split()}
print(words)