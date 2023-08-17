m=int(input("enter the number of rows"))
n=int(input("enter the column"))
mat=[]
X=[]
Y=[]
for i in range(0,m):
    mat+=[0]
    print(mat)
for i in range(0,m):
    mat[i]=[0]*n
    print(mat[i])
for i in range(0,m):
    X+=[0]
    print(X)
for i in range(0,m):
    X[i]=[0]*n
    print(X[i])
for i in range(0,m):
    Y+=[0]
    print(Y)
for i in range(0,m):
    Y[i]=[0]*n
    print(Y[i])


for i in range(0,m):
    for j in range(0,n):
        print("entry in row:",i+1,"column :",j+1)
        X[i][j]=int(input())
        Y[i][j]=int(input())

for i in range(0,m):
    for j in range(0,n):
        mat[i][j]=X[i][j]+Y[i][j]
print(mat)

