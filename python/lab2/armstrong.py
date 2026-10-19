import math
n=int(input(" enter num  :"))
for k in range(1,n):
 num=str(k)
 ans=0
 for i in range(0,len(num)):
    ans+=pow(int(num[i]),len(num))
 if(ans==int(num)):
   print(ans)
