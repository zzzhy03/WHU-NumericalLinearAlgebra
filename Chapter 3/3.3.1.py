import numpy as np

def house(x):
    n = len(x)
    x = x.reshape(n,1)
    eta = np.linalg.norm(x,ord=2)
    x = x / eta
    v = np.zeros(n).reshape(n,1)
    v[1:n] = x[1:n]
    sigma = np.dot(x[1:n].T, x[1:n])
    if sigma == 0:
        beta = 0
    else:
        alpha = (x[0] ** 2 + 1)**(1/2)
        if x[0] <= 0:
            v[0] = x[0] - alpha
        else:
            v[0] = -sigma/(x[0] + alpha)
        beta = 2*v[0]**2 / (sigma + v[0]**2)
        v = v / v[0]
    return v,beta

m = int(input("请输入矩阵行数m:"))
n = int(input("请输入矩阵列数n:"))
#A = np.zeros((m,n))
"""
for i in range(0,m):
    p=input("请输入矩阵的第 %d 行:"%(i+1)).split(' ')
    for j in range(0,n):
        A[i,j]=float(p[j])
"""
A = np.random.rand(m*n) * 10

A = A.reshape((m, n))
for i in range(m):
    for j in range(n):
        A[i,j] = int(A[i,j])
print(A)
tmp = np.matrix(A)
d = []
for i in range(min(n, m-1)):
    v, beta = house(A[i:m, i])
    w = (beta * np.dot(A[i: m, i: n].T, v))
    w = w.reshape(len(w), 1)
    A[i: m, i: n] = A[i:m, i: n] - np.dot(v, w.T)
    d.append(beta)
    A[i+1:m, i] = v[1:m-i, 0]

Q = np.eye(m)
R = np.matrix(A)

for i in range(0, min(n, m-1)):
    v = np.zeros((m, 1))
    v[i, 0] = 1
    v[i+1:m, 0] = A[i+1:m, i]
    Q = np.dot(Q, np.eye(m)-d[i] * np.dot(v, v.T))
    R[i+1:m, i] = 0
print(Q)
print(R)
print(np.dot(Q, R))
