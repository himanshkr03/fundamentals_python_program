a=open(r'F:\hr.txt',"r")
c=a.readline()
l=len(c)
print("the length of c is",l)
count=0
while c:
    for i in range(0,l):
        if c[i]>= 'A' and c[i]<='Z':
            count=count+1
    c=a.readline()
    l=len(c)
print("total number of upper case letter are",count)
