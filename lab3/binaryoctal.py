binary=input("enter binary digits:")
lefto=""
righto=""
left,right=binary.split('.')
i=2
while(i>0):
    if(len(left)%3!=0):
        left="0"+left
    if(len(right)%3!=0):
        right=right+"0"
    i-=1
for ch in range(0,len(left),3):
    ch=left[ch:ch+3]
    if(ch=="000"):
        lefto+="0"
    elif(ch=="001"):
        lefto+="1"
    elif(ch=="010"):
        lefto+="2"
    elif(ch=="011"):
        lefto+="3"
    elif(ch=="100"):
        lefto+="4"
    elif(ch=="101"):
        lefto+="5"
    elif(ch=="110"):
        lefto+="6"
    elif(ch=="111"):
        lefto+="7"
for ch in range(0,len(right),3):
    ch=right[ch:ch+3]
    if(ch=="000"):
        righto+="0"
    elif(ch=="001"):
        righto+="1"
    elif(ch=="010"):
        righto+="2"
    elif(ch=="011"):
        righto+="3"
    elif(ch=="100"):
        righto+="4"
    elif(ch=="101"):
        righto+="5"
    elif(ch=="110"):
        righto+="6"
    elif(ch=="111"):
        righto+="7"

print("octal no:"+lefto+"."+righto)
