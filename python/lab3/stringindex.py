s1=input("enter sentence:")
s2=input("enter a word to find:")
start=s1.find(s2)
if(start==-1):
    print("word not found")
else:    
    end=start+len(s2)-1
    print("word:",s2)
    print("starting index:",start)
    print("ending index:",end)

