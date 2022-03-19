##算法1.1.2
import numpy as np
n=int(input("请输入矩阵阶数:"))
U=np.zeros((n,n))
for i in range(0,n):
    p=input("请输入矩阵的第 %d 行:"%(i+1)).split(' ')
    for j in range(0,n):
        U[i][j]=float(p[j])
y=np.zeros(n)
p=input("请输入向量b:").split(' ')
for i in range(0,n):
    y[i]=float(p[i])

for j in range(n-1,0,-1):
    y[j]=y[j]/U[j][j]
    y[0:j]=y[0:j]-y[j]*U[0:j,j]
y[0]=y[0]/U[0,0]
print(y)
