a=int(input("enter the number "))
c=0
rev=0
while a>0:
    c=a%10
    rev=rev+int(c/10)
    print(rev)
