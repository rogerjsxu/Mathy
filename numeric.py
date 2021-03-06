# some numerical algorithms
from linalg import *
from basic import *

########### Numerical Analysis ##########
# --------- Linear Algebra ----------
## A = LU decomposition
'''
import numpy as np
from scipy.linalg import lu
A = np.array([0,0,1,2,0,0,3,0,1,-1,0,1,2,0,-1,3]).reshape(4,4)
a,b,c= lu(A)
print(a)
print(b)
print(c)
'''

# A = LU decomposition
def lu(A): # 仅限于各阶主子式都不为零，否则需要使用plu分解
    # A 必须是方阵
    L = eyes(len(A))
    U = zeros(len(A),len(A))
    
    def sum_u(L,U,k,j):
        s = 0
        for m in range(k):
            s += L[k][m]*U[m][j]
        return s
    def sum_l(L,U,k,i):
        s = 0
        for m in range(k):
            s += L[i][m]*U[m][k]
        return s
    
    for k in range(len(A)):
        # 求U的第k行 (实际上是k+1)
        for j in range(k,len(A)):
            U[k][j] = (A[k][j] - sum_u(L,U,k,j)) / L[k][k]                                  # / L[k][k] 可删，为保持与U的对称性

        # 求L的第k列 (实际上是k+1)
        for i in range(k,len(A)):
            L[i][k] = (A[i][k] - sum_l(L,U,k,i)) / U[k][k]
    return L,U

# A = PLU decomposition
#失败，PA之后还是有0主元的情况，不知问题出在那里##
def plu(A): #
    print("Waring: This algorithm is not well implemented")
    P = eyes(len(A))    
    for j in range(len(A)):
        max_index = j
        max_item = 0
        print(j,'round')
        for i in range(j,len(A)):
            if abs(max_item) < abs(A[i][j]): # 列选主元，其实不必最大，只要主元！=0即可，不知是不是这里的问题
                max_item = A[i][j]
                max_index = i
        if max_index != j:
            A = exchange_rows(A,j,max_index)
            P = exchange_rows(P,j,max_index)
            print("exchanged",j,'and',max_index)
            for k in range(j+1,len(A)):
                A = add_rows_by_factor(A,k,-A[k][j]/A[j][j],j)
                print('消掉：',k)
                print_matrix(A)
    print_matrix(P,name = "P")
    L,U = lu(multiply(P,A))
    return transpose(P),L,U


# Cholesky decomposition
def cholesky(A, mode = 'LLT'):
    L,U = lu(A)
    #print_matrix(L,name = "L = ")
    #print_matrix(U,name = "U = ")
    L_T = U
    D = zeros(len(A),len(A))
    for i in range(len(A)):
        D[i][i] = U[i][i]
        for j in range(i,len(A)):
            U[i][j]/=U[i][i]
    if mode == 'LDLT':
        return L,D,L_T
    if mode == 'LLT':
        D_sqrt  = D
        for i in range(len(A)):
            D_sqrt[i][i] = sqrt(D_sqrt[i][i])
        return multiply(L,D_sqrt),multiply(D_sqrt,L_T)


## 线性方程组的迭代法
# 线性方程组的解法 一般记法，矩阵记法
def norm_mat(A,):
    pass
# decompose A into D-L-U
def dlu_decompose(A):
    D = zeros(len(A),len(A))
    L = zeros(len(A),len(A))
    U = zeros(len(A),len(A))
    for i in range(len(A)):
        D[i][i] = A[i][i]
    for j in range(len(A)):
        for i in range(j+1,len(A)):
            L[i][j] = -A[i][j]
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            U[i][j] = -A[i][j]
    return D,L,U

# 计算谱半径，有助于判断收敛性，用到了sympy 的复数模块
def spectral_radius(A):
    eigens = eigen_value(A) # 如果返回复数，是sympy.I
    print(eigens)
    max_value = 0
    for value in eigens:
        if sympy.Abs(value) > max_value:
            max_value = sympy.Abs(value) # 使用sympy 求模
    return max_value    # 谱半径：特征值模的最大值   

# 传入A,b 计算雅可比迭代，若不收敛则报错
def jacobi_iteration(A,b,epochs=20):
    D,L,U = dlu_decompose(A)
    print_matrix(D,name = "D")
    print_matrix(L,name = "L")
    print_matrix(U,name = "U")
    B1 = multiply(inv(D), add_mat(L, U))
    print_matrix(B1,name = "B1 Jacobi matrix")
    s_radius = spectral_radius(B1)
    print("spectral radius: ",s_radius)
    if s_radius >=1:    # 若没有收敛，报错
        raise ValueError("spectral_radius >= 1, not converging!")
    g1 = multiply(inv(D), b)
    x = zeros(len(A),1)
    for i in range(epochs):
        x = add_mat(multiply(B1,x), g1)
        # print_vector(x)
    return x

def gauss_seidel_iteration(A,b,epochs=20):
    '''
    B2=(D-L)^(-1)*U
    g2=(D-L)^(-1)*b
    x=B2*x+g2
    '''
    D,L,U = dlu_decompose(A)
    print_matrix(D,name = "D")
    print_matrix(L,name = "L")
    print_matrix(U,name = "U")
    B2 = multiply(inv(sub_mat(D,L)),  U)
    print_matrix(B2,name = "B2 Gauss-Seidel matrix")
    s_radius = spectral_radius(B2)
    print("spectral radius: ",s_radius)
    if s_radius >=1:
        raise ValueError("spectral_radius >= 1, not converging!")
    g2 = multiply(inv(sub_mat(D,L)), b)
    x = zeros(len(A),1)
    for i in range(epochs):
        x = add_mat(multiply(B2,x), g2)
        # print_vector(x)
    return x

# 松弛法
def sor_iteration(A,b,w,epochs=20): # gauss_seidel 是一种特例
    pass

### 计算特征值
# 瑞利商，可以帮助计算特征值
def rayleigh(A,x):
    return multiply(transpose(x),A,x)[0][0]/multiply(transpose(x),x)[0][0]

# 幂迭代法 根据《数值分析萨奥尔中译本》第12章 （课本上稍有不同）
def power_iteration(A,x,epochs=20):
    for i in range(epochs):
        u = times_const(1/norm(x),x) # 我们输入的向量归一化
        x = multiply(A,u) # 输入的任意向量，经过足够多次数乘矩阵，方向接近于特征向量
        lam = multiply(transpose(u),x) # 实际上到这一步，求得是瑞利商
        print("---epoch",i,"---")
        print("Eigenvalue",lam)
        print_vector(u)
    return lam,u # 返回特征值和特征向量

A1 = [[3,-4,3],[-4,6,3],[3,3,1]]
power_iteration(A1,[[1],[1],[1]])

A2 = [[4,2,2],[2,5,1],[2,1,6]]
power_iteration(A2,[[1],[1],[1]])



# 反幂迭代法 
def inv_power_iteration(A,x,epochs=10,method = "inv"):

    for i in range(epochs):
        u = times_const(1/norm(x),x)
        
        lam = multiply(transpose(u),A,u)
        
        x = solve_linear_equation(sub_mat(A,times_const(lam[0][0],eyes(len(A)))),u)
        print("epoch",i,": ",lam)
    return lam




if __name__ == '__main__':

    '''
    A1 = [[1,2,-4],[1,1,2],[1,1,1]]
    b = randmat(3,1)
    print(rayleigh(A1,b))
    jacobi_iteration(A1,b)
    '''
    '''
    A2 = [[1,-2,1],[3,1,4],[2,-1,1]]
    A3 = [[1,2,-2],[1,1,1],[2,2,1]]
    
    jacobi_iteration(A3,b)
    '''
    











    '''
    # 使用自己实现的函数计算第六题的LU分解        
    A = [[2,1,-4],[1,2,2],[-4,2,20]]
    L,U=lu(A)
    print("A的LU分解")
    print_matrix(L,name = 'L', precision=3)
    print_matrix(U,name = 'U', precision=3)
    b=[[-1],[0],[4]]
    y = solve_linear_equation(L,b)
    x = solve_linear_equation(U,y)
    print("方程组的解为")
    print_vector(x)
    '''



    '''
    ###矩阵的cholesky分解测试
    A = [[1,2,-2],
        [2,5,-3],
        [-2,-3,21]] 
    a,c = cholesky(A,mode = "LLT")
    print_matrix(a,name = "L")
    print_matrix(c,name = "LT")

    print_matrix(multiply(a,c))#multiply(b,c)))


    '''