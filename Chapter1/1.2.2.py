import numpy as np
n=int(input("请输入矩阵阶数:"))
A=np.zeros((n,n))
for i in range(0,n):
    p=input("请输入矩阵的第 %d 行:"%(i+1)).split(' ')
    for j in range(0,n):
        A[i][j]=float(p[j])
u=[]
for k in range(0,n-1):
    p=np.where(A==np.max(A[k:n,k]))
    temp=A[k,:].copy()
    A[k,:]=A[p[0][0],:]
    A[p[0][0],:]=temp
    u.append(p[0][0])
    if A[k][k]!=0:
        A[k+1:n,k]=A[k+1:n,k]/A[k][k]
        A[k+1:n,k+1:n]=A[k+1:n,k+1:n]-np.dot(A[k+1:n,k].reshape(n-k-1,1),A[k,k+1:n].reshape(1,n-k-1))
    else:
        break
print(np.array(u)+1)
L=np.zeros((n,n))
for i in range (0,n):
    L[i][i]=1
    for j in range (0,i):
        L[i][j]=A[i][j]
        A[i][j]=0

print("L:")
print(L)
print("U")
print(A)
print("L*U (交换前)")
print(np.dot(L,A))
print("")
A1=np.dot(L,A)
for k in range(n-2,-1,-1):
    temp=A1[k,:].copy()
    A1[k,:]=A1[u[k],:]
    A1[u[k],:]=temp
print("L*U (交换后)")
print(A1)