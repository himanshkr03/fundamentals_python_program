f=open(r'F:\exam.txt',"w")
l1="welcome to python class"
f.write(l1)
l2="\ngive the answer carefully"
f.write(l2)
f.close()
f=open(r'F:\exam.txt',"r")
text=f.readline(7)
print(text)
f.close()
