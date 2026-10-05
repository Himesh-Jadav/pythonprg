l=[1,0,1,0,0,1]
a=l.count(1)
o=l.count(0)
n=int(input("enter number of block you want to insert "))
if(o==len(l)):
    print(" memory is occupied ")
else:
    if(n>a):
        print(" there is not enough space to store all blocks ")
    i=0
    while(i!=len(l) and n>0):
            if(l[i]==1):
             l[i]=0
             n-=1
            i+=1
    if(n>0): 
        print(f"only {a} blocks are stored  ")
    else :
        print(" all blocks are stored succesfully ")
                
                
        