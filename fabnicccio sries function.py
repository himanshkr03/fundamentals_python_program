def xyz(n):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(3,n+1):
        c=a+b
        a=b
        b=c
        print(c)
n=int(input("enter the number"))
xyz(n)

