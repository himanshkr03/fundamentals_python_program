def add(n,s):
    if n==0:
        return s
    else:
        s=s+n
        n=n-1
        return add(n,s)
n=10
s=0 
p=add(n,s)
print(p)

