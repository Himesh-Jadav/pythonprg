marks = {
    101: ['a', 'b', 'b', 'a', 'c', 'd', 'd', 'a', 'b', 'a'],
    102: ['b', 'b', 'b', 'a', 'b', 'b', 'c', 'c', 'c', 'c']
}

ans = ['a', 'b', 'b', 'a', 'c', 'd', 'd', 'a', 'b', 'a']

result = {}

for key, value in marks.items():
    count = 0
    for i in range(len(ans)):
        if value[i] == ans[i]: 
            count = count + 1
        else:
            count = count - 0.25
    result[key] = count
    print("Roll No: ", key, " Marks Scored: ", count)
    
print(result)