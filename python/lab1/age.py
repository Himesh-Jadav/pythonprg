#  current date
d=int(input(" enter date  : "))
m=int(input(" enter month : "))
y=int(input(" enter year :  "))

#date of birth
d1=int(input(" enter date  : "))
m1=int(input(" enter month : "))
y1=int(input(" enter year :  "))

if(d<d1 and(m==2 or m==4 or m==6 or m==8 or m==9 or m==11 or m==1)):
       d+=31
       m-=1
elif(d<d1 and(m==5 or m==7 or m==10 or m==12)):
       d+=30
       m-=1
elif(y%100==0):
    if(y%400):
       d+=29
       m-=1 
elif(y%4==0):
     d+=28
     m-=1
if(m<m1):
     m+=12
     y-=1
d3=d-d1
m3=m-m1
y3=y-y1
print(f" my current age is {y3} YEAR {m3} month {d3} days ")
           
