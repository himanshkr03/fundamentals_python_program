X=[]
Y=[]
for i in range(0,3):
    X+=[0]
    Y+=[0]
for i in range(0,3):
    for j in range(0,3):
        X[i][j]=int(input("enter the matrix : "))
        Y[i][j]=int(input("enter the matrix : "))
for i in range(len(X)):
    for j in range(len(Y[0])):
        result[i][j]=X[i][j]+Y[i][j]
for r in result:
    print(result)
