import numpy as np
n=int(input("请输入矩阵阶数:"))
A=np.zeros((n,n))
for i in range(0,n):
    p=input("请输入矩阵的第 %d 行:"%(i+1)).split(' ')
    for j in range(0,n):
        A[i][j]=float(p[j])

for k in range(0,n):
    A[k,k]=A[k,k] ** 0.5
    A[k+1:n,k]=A[k+1:n,k]/A[k][k]
    for j in range(k+1,n):
        A[j:n,j]=A[j:n,j]-A[j:n,k]*A[j,k]

L=np.zeros((n,n))
for i in range (0,n):
    for j in range (0,i+1):
        L[i][j]=A[i][j]

print("L:")
print(L)
print("L.T")
print(L.T)
print("L*L.T")
print(np.dot(L,L.T))