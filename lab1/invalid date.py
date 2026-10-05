d=int(input(" enter date " ))
m=int(input(" enter month  " ))
y=int(input(" enter year  " ))
if(d<1 or d >31):
  print(" invalid date! ")
elif(m<1 or m>12 or year<1):
  print( " invalid date " )
if((m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12) and d>31):
    print(" invalid date !")
elif((m==4 or m==6 or m==9 or m==11) and d>30):
    print( " invalid date ")
elif(y%100==0):
    if(y%400):
        if(d>29):
          print(" invalid date ")

    else:
        if(d>28):
          print(" invalid date ")
elif(y%4==0 and d>29):
    print(" invalid date ")
    
    
