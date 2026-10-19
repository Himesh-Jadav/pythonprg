s = input("Enter sentence: ")
print(s)
words = {word: word[1:] + word[0] + 'o' 
         for word in s.split()
         }
for i in words.items():
    print(i)