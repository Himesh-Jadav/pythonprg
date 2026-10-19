# quadratic is in form of ax^2+bx+c=0
import cmath
a=int(input("Enter value of a " ))
b=int(input("Enter value of b " ))
c=int(input("Enter value of c " ))

root1=(-b+cmath.sqrt(b*b-4*a*c))/2
root2=(-b-cmath.sqrt(b*b-4*a*c))/2
print(f"First root is {root1} and second root is {root2}")
      
