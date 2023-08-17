print("python programme to print fibonacci series using recurssion")
def fibo(x):
    if x<=1:
        return x
    else:
        return(fibo(x-1)+fibo(x-2))
n=int(input("enter the number of term :"))
if n<= 0:
    print("please enter the positive integer ")
else:
    for i in range(n):
        print(fibo(i))
