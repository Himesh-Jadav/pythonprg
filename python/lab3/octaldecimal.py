octal=input("enter octal no:")
left,right=octal.split(".")
print(left)
leftd=0
left=int(left)
i=0
while(left>0):
    leftd=leftd+((left%10)*(8**i))
    left=left/10
    i+=1
print(leftd)
