print("read file line by line")
a=open(r'F:\hr.txt',"r")
c=" "
while c:
    c=a.readline()
    print(c,end=" ")
a.close()
