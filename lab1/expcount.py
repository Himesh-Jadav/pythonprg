exp=input("enter expression:")
tsum=float(input("enter time for '+':"))
tsub=float(input("enter time for '-':"))
tmul=float(input("enter time for '*':"))
tdiv=float(input("enter time for '/':"))

csum=exp.count('+')
csub=exp.count('-')
cmul=exp.count('*')
cdiv=exp.count('/')
totaltime=csum*tsum+csub*tsub+cmul*tmul+cdiv*tdiv
print("total '+' count {} \n total '-' count {} \n total '*' count {} \n total '/' count {}".format(csum,csub,cmul,cdiv))
print(f'total time for evalution of expression is {totaltime}s')
