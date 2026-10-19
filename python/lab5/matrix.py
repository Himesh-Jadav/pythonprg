m1 = [[5, 4, 9], [3, 7, 8], [74, 3, 55]]
m2 = [[3, 4, 2], [3, 8, 1], [2, 5, 6]]

add = []
sub = []
mul = []

# Addition
for i in range(3):
    l = []
    for j in range(3):
        l.append(m1[i][j] + m2[i][j])
    add.append(l)

print("Addition:", add)

# Subtraction
for i in range(3):
    l = []
    for j in range(3):
        l.append(m1[i][j] - m2[i][j])
    sub.append(l)

print("Subtraction:", sub)

# Multiplication
for i in range(3):
    l = []
    for j in range(3):
        s = 0
        for k in range(3):
            s += m1[i][k] * m2[k][j]
        l.append(s)
    mul.append(l)

print("Multiplication:", mul)

# Trace
s = 0
for i in range(3):
    s += m1[i][i]

print("Trace:", s)

# Transpose
t = []
for i in range(3):
    l = []
    for j in range(3):
        l.append(m1[j][i])
    t.append(l)

print("Transpose:", t)