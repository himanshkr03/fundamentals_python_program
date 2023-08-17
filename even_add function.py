s=0
def even_add(n):
    if n==0:
        return 0
    elif n%2==0:
        for i in range(0,n+1,2):
            s=s+i
        print(s)
a=int(input("entr the number"))
print("the computed result is",even_add(a))
