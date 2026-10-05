# quadratic is in form of ax^2+bx+c=0
import cmath
a=int(input(" enter value of a " ))
b=int(input(" enter value of b " ))
c=int(input(" enter value of c " ))

root1=(-b+cmath.sqrt(b*b-4*a*c))/2
root2=(-b-cmath.sqrt(b*b-4*a*c))/2
print(f"first root is {root1} and second root is {root2}")
      
