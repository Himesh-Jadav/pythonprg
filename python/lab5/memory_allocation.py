memory=[1,0,1,0,0,1]
n = int(input("How many blocks to store?: "))
empty = a.count(0)
if n <= empty:
    for i in range(len(memory)):
        if a[i] == 0 and > 0:
            a[i] == 1
            n -= 1
    print("Blocks stored successfully")
    print("Updated list: ", memory)
else:
    print("Memory Full")
                
                
        