##算法1.1.1
import numpy as np
n=int(input("请输入矩阵阶数:"))
L=np.zeros((n,n))
for i in range(0,n):
    p=input("请输入矩阵的第 %d 行:"%(i+1)).split(' ')
    for j in range(0,n):
        L[i][j]=float(p[j])
b=np.zeros(n)
p=input("请输入向量b:").split(' ')
for i in range(0,n):
    b[i]=float(p[i])

for j in range(0,n-1):
    b[j]=b[j]/L[j][j]
    b[j+1:n]=b[j+1:n]-b[j]*L[j+1:n,j]
b[n-1]=b[n-1]/L[n-1,n-1]

print(b)