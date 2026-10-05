l=[]
k=[]
l.append(["22 oct 26",99])
l.append(["22 oct 26",101])
for i in range(len(l)):
  n=0
  for j in range(len(k)):
    if l[i][0] in k[j]:
      k[j][1]+=l[i][1]
      n=1
      break
  if(n==0):
    k.append(l[i])
print(k)


    
