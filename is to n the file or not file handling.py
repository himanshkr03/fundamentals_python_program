f=0
print("is ","to","is present in the file or not")
a=open(r'F:\hr.txt',"r")
c=a.readline()
l=len(c)
print("the length of c is",l)
count=0
while c:
    for i in range(0,l):
        if c[i]=="t" and c[i+1]=="o":
            count+=1
            f=1
    c=a.readline()
    l=len(c)
print("the total number of [to] in the file is",count)
if f==1:
    print("found")
else:
    print("not found !!!!!!!!!!!!!")
        
            
