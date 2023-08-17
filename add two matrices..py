A=[]
n=int(input("enter N for N x N matrix :"))
print("enter the eleement")
for i in range(n):
    row=[]
for j in range(n):
    row.append(int(input()))
A.append(row)
print(A)
print("display array in matrix form")
for i in range(n):
    for j in range(n):
        print(A[i][j],end=" ")
        print()
B=[]
n=int(input("enter N for N x N matrix :"))
print("enter the element")
for i in range(n):
    row=[]
    for j in range(n):
        row.append(int(input()))
    B.append(row)
print(B)
print("disply array in matrix form")
for i in range(n):
    for j in range(n):
        print(B[i][j],end=" ")
    print()
result=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(n):
    for j in range(len(A[0])):
        result=[i][j]=A[i][j]+B[i][j]
print("result in matrix form")
for r in result:
    print("result in matrix form",r)
