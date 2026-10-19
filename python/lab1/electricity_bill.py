# unit used is k
k=int(input(" enter unit used "))
if(k<=100):
   print(" electricity bill is :" ,k*0.25)
elif(k>100 and k<=200):
   print(" electricity bill is :" ,k*0.5)
elif(k>200 and k<=300):
   print(" electricity bill is :" ,k*0.75)
elif(k>300 and k<=400):
   print(" electricity bill is :", k*1)
else:
   print(" electricity bill is :", k*1.5)
