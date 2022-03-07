# Assignment1 
## 1.给出求下三角矩阵的详细算法.

## 2.设$S,T\in R^{n*n} $ 为两个上三角阵，而且线性方程组 $ (ST-\lambda I)x=b $ 也是非奇异的，试给出一种运算量为$ O(n^{2}) $ 的算法来求解该方程组.

## 3.证明：如果$L_{k}=I-l_{k}e_{k}^{T} $是一个Gauss变换，则 $L_{k}^{-1} = I+I-l_{k}e_{k}^{T}$ 也是一个Gauss变换.

## 4.确定一个$3*3$ Gauss变换$L$,使得$$ L\begin{bmatrix}2\\3\\4 \end{bmatrix} =\begin{bmatrix}2\\7\\8 \end{bmatrix} $$

## 5.证明：如果$A\in R^{n*n} $ 有三角分解，并且是非奇异的，那么定理1.1.2中的$L$和$U$都是非奇异的.

## 6.设$A=[a_{ij}]\in R^{n*n} $的定义如下：$$ a_{ij}=\begin{cases}1, \ 如果i=j或j=n \\ -1, \ 如果i>j \\ 0, 其他\end{cases} $$ 证明：$A$ 有满足$\lvert l_{ij}\rvert \leq 1$ 和 $u_{n,n}=2^{n-1} $的三角分解.

## 7.设$A$对称且$a_{1 1}\neq0 $ 并假设经过一步Gauss消去后，$A$具有如下形状:$$ \begin{bmatrix}a_{11} \ a_{1}^{T} \\ 0 \ A_{2} \end{bmatrix} $$ 证明：$A_{2}$仍是对称矩阵.

## 8.设$A=[a_{ij}]\in R^{n*n}$是严格对角占优阵，即$A$满足$$ \lvert a_{kk}\rvert > \sum_{j=1 \ j\neq k}^{n} \lvert a_{kj} \rvert, k=1,...,n, $$ 又经过一步Gauss消去之后，A具有如下形状：$$ \begin{bmatrix} a_{11}\ a_{1}^{T} \\ 0 \ A_{2}  \end{bmatrix}$$ 试证明：矩阵$A_{2}$仍然是严格对角占优阵.由此推断：对于对称的严格对角占优阵来说，用Gauss消去法和列主元Guass消去法可得到同样的结果。
