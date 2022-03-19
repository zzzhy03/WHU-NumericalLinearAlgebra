import numpy as np
n=int(input("请输入矩阵阶数:"))
A=np.zeros((n,n))
for i in range(0,n):
    p=input("请输入矩阵的第 %d 行:"%(i+1)).split(' ')
    for j in range(0,n):
        A[i][j]=float(p[j])

for j in range(0,n):
    print(j)
    v=[]
    for i in range(0,j):
        v.append(A[j,i]*A[i,i])
    Vt=np.array(v)
    if j==0:
        A[j+1:n,j]=(A[j+1:n,j]/float(A[j,j])).reshape(n-j-1)
    elif j==n-1:
        A[j,j]=A[j,j]-np.dot(A[j,0:j].reshape(1,j),Vt[0:j].reshape(j,1))
    else:
        A[j,j]=A[j,j]-np.dot(A[j,0:j].reshape(1,j),Vt[0:j].reshape(j,1))
        A[j+1:n,j]=((A[j+1:n,j].reshape(n-j-1,1)-np.dot(A[j+1:n,0:j],(Vt[0:j].reshape(j,1))))/float(A[j,j])).reshape(n-j-1)
L=np.zeros((n,n))
D=np.zeros((n,n))
for i in range (0,n):
    D[i][i]=A[i][i]
    L[i][i]=1
    for j in range (0,i):
        L[i][j]=A[i][j]

print("L:")
print(L)
print("L.T")
print(L.T)
print("D")
print(D)
print("L*D*L.T")
print(np.dot(np.dot(L,D),L.T))