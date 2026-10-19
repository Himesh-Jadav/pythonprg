def power(n):
     if(n==0):
        return 1
     return 10* power(n-1)
n=int(input(" enter yr number : "))
count=0
ans=0
while(n!=0):
    rem=n%2
    ans+=rem*power(count)
    n=int(n/2)
    count+=1
print(ans)
    
    
