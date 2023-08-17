m=2
n=2
mat=[]
for i in range(0,m):
    mat+=[0]
for i in range(0,m):
    mat[i]=[0]*n
for i in range(0,m):
    for j in range(0,n):
        print("entry in row:",i+1,"column :",j+1)
        mat[i][j]=int(input())
print(mat)
    
