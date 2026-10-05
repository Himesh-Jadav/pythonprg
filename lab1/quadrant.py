x=int(input(" enter x coordinate of point : "))
y=int(input(" enter y coordinate of point : "))
if(x>0 and y>0):
    print(" point is in first quadrant ")
elif(x<0 and y>0):
    print(" point is in second quadrant ")
elif(x<0 and y<0):
    print(" point is in third quadrant ")
elif(x>0 and y<0):
    print(" point in fourth quadrant ")
elif(x==0 and y==0):
    print(" point is at origin  ")
elif(x==0 and y>0):
    print(" point is on +ve y axiis  ")

elif(x==0 and y<0):
    print(" point is on -ve y axis ")

elif(x>0 and y==0):
    print(" point is on +ve x axis ")
elif(x>0 and y==0):
    print(" point is on -ve x axis  ")
