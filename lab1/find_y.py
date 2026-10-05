def power(num,pow):
   if(pow==0):
      return 1
   return num*power(num,pow-1)
x=int(input(" enter value of x :"))
n=int(input("enter value of n "))
y=0;
if(n==0):
    y=x
elif(n==1):
    y=x+1
elif(n==2):
    y=x*x+no
else:
    y=power(x,n)
print(y)