s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
prefix = ""
i = 0
while i < len(s1) and i < len(s2):
    if s1[i] == s2[i]:
        prefix += s1[i]
        i += 1
    else:
        break
print("Longest common prefix:", prefix)
