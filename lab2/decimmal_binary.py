s=input(" enter the number  ")
i=int(s.split('.')[0])
f=int(s.split('.')[1])
cout=len(s.split('.')[1])
i_ans=""
f_ans=""
while(i!=0):
    rem=str(i%2)
    i=i//2
    i_ans=rem+i_ans
k =f
while(f%pow(10,cout)!=0 and f!=k):
    un=f*2//pow(10,cout)
    f=f*2%pow(10,cout)
    f_ans+=str(un)
    
print(i_ans+'.'+f_ans)