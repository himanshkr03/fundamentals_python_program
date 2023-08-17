s=1
def fact(a,s):
        for i in range(1,a+1):
            s=s*i
        return s
a1=int(input("enter the number"))
c=fact(a1,1)
print(c)
