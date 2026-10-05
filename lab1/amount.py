n=int(input(" enter number of students " ))
amount=0
for i in range(1,n+1):
 if(i>99):
    amount+=i%100
 else:
    amount+=i
print(f" amount to be collected from all students is {amount} ")
