import math
print("quadratic equation is in  the form of ax**2+bx+c=0,enter cofficient below")
a=int(input("enter the value of a : "))
b=int(input("enter the value of b : "))
c=int(input("enter the value of c : "))
if a==0:
    print("the value of a should not be zero")
else:
    delta=b*b - 4*a*c
    print("delta=b*b - 4*a*c=",delta)
    if delta>0:
        root1=(-b+math.sqrt(delta))/(2*a)
        root2=(-b-math.sqrt(delta))/(2*a)
        print("ROOT 1=",root1,"ROOT 2=",root2)
        print("root are real and unequal")
    elif delta==0:
        root1=-b/2*a
        print("ROOT 1=",root1,"ROOT 2=",root1)
        print("root are real and equal")
    else:
        print("root are complex and imaginary")
        
