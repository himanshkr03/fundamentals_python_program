def check_num(x):
    if x>0:
        print(x,"is a positive integer")
    elif x<0:
        print(x,"is a negative integer")
    elif x==0:
        print("entered number is nithe negative nor positive")
a=int(input("enter the number to check either the number is positive negative or zero : "))
c=check_num(a)
