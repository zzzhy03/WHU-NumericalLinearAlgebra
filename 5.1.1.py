import numpy as np
n = int(input("请输入矩阵阶数:"))
def is_pos_def(x):
    return np.all(np.linalg.eigvals(x) > 0)

def getsym(n):
    A = np.random.rand(n*n).reshape((n, n))
    for i in range(n):
        for j in range(i,n):
            A[i, j] = int(A[i, j] * 10)
            A[j, i] = A[i, j]
    return A

A = np.zeros((n, n))
A = getsym(n)

while is_pos_def(A)!=True:
    A = getsym(n)

b = np.random.rand(n).reshape((n, 1))
for i in range(n):
    b[i] = b[i] * 100
    b[i] = int(b[i])
print(A)
print(b)

print(np.dot(np.linalg.inv(A), b))


x = np.zeros(n).reshape((n, 1))
r = b - np.dot(A, x)
k = 0
while np.linalg.norm(r)!=0:
    k = k + 1
    alpha = np.dot(r.T, r)/(np.dot(np.dot(r.T, A), r))
    x = x + alpha * r
    r = b - np.dot(A, x)
print(x)
print(np.dot(A, x))