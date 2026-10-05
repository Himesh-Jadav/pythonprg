n=int(input(" enter value of n : "))
for i in range(2,n+1):
    flag=True
    j=i-1
    while(j>1):
      if(i%j==0):
         flag=False
         break
      j-=1
    if(flag):
     print(i)