n = int(input("Enter any number : "))
r = 0
while n>0:
    r = r*10+n%10
    n = int(n/10)
    print(r,n)
