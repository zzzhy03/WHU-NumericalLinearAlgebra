import numpy as np

p = input("请输入向量x:").split(' ')
n = len(p)
x = np.zeros(n).reshape(n,1)
v = np.zeros(n).reshape(n,1)
for i in range(0,n):
    x[i] = float(p[i])
xx = np.matrix(x)


eta = np.linalg.norm(x,ord=2)
x = x / eta
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

H = np.eye(n) - beta * np.dot(v,v.T)
print(v)
print(H)
print(beta)
print(np.dot(H,xx))