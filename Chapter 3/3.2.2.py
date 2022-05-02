import numpy as np
p = input("请输入向量x:").split(' ')
n = len(p)
x = np.zeros(n).reshape(n,1)
for i in range(0,n):
    x[i] = float(p[i])

p = int(input("请输入p(变化)"))
q = int(input("请输入q(置0)"))
a = x[p-1]
b = x[q-1]
c = 1
s = 0
if b!=0:
    if abs(b) > abs(a):
        t = a/b
        s = 1/((1 + t ** 2)**(0.5))
        c = s * t
    else:
        t = b/a
        c = 1/((1 + t ** 2)**(0.5))
        s = c * t
x.reshape(n,1)
G = np.eye(n)
G[p-1,p-1]=c
G[p-1,q-1]=s
G[q-1,p-1]=-s
G[q-1,q-1]=c
print(G)
print(np.dot(G,x))