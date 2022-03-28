import numpy as np

n=1000
B=np.random.rand(n*n)
B=B*1000000
for i in range(n*n):
   B[i]=round(B[i])
B=B.reshape(n,n)
print(B)
B=B.reshape(n,n)
x=np.zeros(n)
x[0]=1## 默认使第一个为1
k=1
cnt=1
while k==1:
   print(k)
   w=np.dot(B,x)
   v=np.sign(w)
   z=np.dot(B.T,v)
   norm_z=np.linalg.norm(z,ord=np.inf)
   t1=np.dot(z.T,x)
   if norm_z <= t1:
      ans=np.linalg.norm(w,ord=1)
      k=0
   if norm_z > t1:
      x=np.zeros(n)
      x[np.argmax(z)]=1
      k=1
      cnt=cnt+1

print(np.linalg.norm(B,ord=1))
print(ans)
print(cnt)