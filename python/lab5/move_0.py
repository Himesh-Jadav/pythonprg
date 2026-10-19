l=[1,0,3,5,46,0,0,6,4]
j = 0
for i in range(len(l)):
    if l[i] != 0:
        swap(l[i],l[j])
        j += 1
print(l)