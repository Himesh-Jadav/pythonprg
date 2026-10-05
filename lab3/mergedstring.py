s1=input("ENTER FIRST STRING:")
s2=input("ENTER SECOND STRING:")
i=0
result=""
while(i<len(s1) and i<len(s2)):
      result+=s1[i]
      result+=s2[i]
      i+=1
if(i<len(s1)):
    result+=s1[i:]
if(i<len(s2)):
    result+=s2[i:]
print("merged string:"+result)
