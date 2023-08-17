def factorial_calc(x):
    if x==1:
        return 1
    else:
        return(x*factorial_calc(x-1))
num=int(input("enter the number : "))
if num<0:
    print("yoy have entered the negative integer ")
elif num>=1:
    if num==1:
        print("factorial of",num,"is",1)
    else:
        print("the factorial of number ",num,"is",factorial_calc(num))
