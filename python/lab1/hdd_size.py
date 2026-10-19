import cmath
def power(num,pow):
   if(pow==0):
      return 1
   return num*power(num,pow-1)
hdd_size=int(input(" enter hdd size in gigaBytes : "))
# no of ytes it cn be hold is :
bytes=cmath.log(1024,2)
print(bytes)