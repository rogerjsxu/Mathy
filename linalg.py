from basic import *

###### linear algebra ######
#print matrix in a more readable way
def print_matrix(A,precision=2,name = 'Matrix'):
    print(name+"[")
    for i in range(len(A)):
        print("\t",end='')
        for j in range(len(A[0])):  
                
            print(format(A[i][j],"."+str(precision)+"f"),end='\t')
        print()
    print(']') 
# auto judge row vector and column vector and print
def print_vector(A,precision=4):

    if(len(A) == 1):
        print("Row Vector[")
        print("\t",end='')
        for j in range(len(A[0])):
            print(format(A[0][j],"."+str(precision)+"f"),end='\t')
        print("\n]")
    elif(len(A[0]) == 1):
        print("Column Vector[")
        for i in range(len(A)):
            print("\t",format(A[i][0],"."+str(precision)+"f"))
        print("]")
    else:
        raise ValueError("NOT a vector!")
# print vector group
def print_vectors(*vec_tuple,precision=4):
    for k in range(len(vec_tuple)):
        if(len(vec_tuple[k]) == 1):
            print("Row Vector(%d)["%(k+1))
            print("\t",end='')
            for j in range(len(vec_tuple[k][0])):
                print(format(vec_tuple[k][0][j],"."+str(precision)+"f"),end='\t')
            print("\n]")
        elif(len(vec_tuple[k][0]) == 1):
            print("Column Vector(%d)["%(k+1))
            for i in range(len(vec_tuple[0])):
                print("\t",format(vec_tuple[k][i][0],"."+str(precision)+"f"))
            print("]")
        else:
            raise ValueError("NOT a vector!")
def print_vector_group(vec_tuple,precision=4):
    for k in range(len(vec_tuple)):
        if(len(vec_tuple[k]) == 1):
            print("Row Vector(%d)["%(k+1))
            print("\t",end='')
            for j in range(len(vec_tuple[k][0])):
                print(format(vec_tuple[k][0][j],"."+str(precision)+"f"),end='\t')
            print("\n]")
        elif(len(vec_tuple[k][0]) == 1):
            print("Column Vector(%d)["%(k+1))
            for i in range(len(vec_tuple[0])):
                print("\t",format(vec_tuple[k][i][0],"."+str(precision)+"f"))
            print("]")
        else:
            raise ValueError("NOT a vector!")
def nulls(col):
    a = []
    for i in range(col):
        a.append([])
    return a
#generates matrix with all zeros
def zeros(row,col):
    '''
    a=[]
    for i in range(row):
        a.append([])
        for j in range(col):
            a[i].append(0)
    return a
    '''
    return [[0 for i in range(col)]for i in range(row)]

#generates matrix with all ones
def ones(row,col):
    '''
    a=[]
    for i in range(row):
        a.append([])
        for j in range(col):
            a[i].append(1)
    return a
    '''
    return [[1 for i in range(col)]for i in range(row)]

#generates identity matrix
def eyes(n):
    a = [[0 for i in range(n)]for i in range(n)]
    for i in range(n):
        a[i][i]=1
    return a
def diag(*a):
    l = len(a)
    A = zeros(l,l)
    for i in range(l):
        for j in range(l):
            if i ==j:
                A[i][j] = a[i]
    return A
def randmat(row,col,largest = 10):#,property = "None"):
    import random
    A = zeros(row,col)
    for i in range(row):
        for j in range(col):
            A[i][j] = random.randint(0,largest)
    return A
def check_matrix_square(A):
    if len(A)==len(A[0]):
        return True
    else:
        return False
#这种转置方式有问题
def transpose(A):
    B = zeros(len(A[0]),len(A))
    #print("after_shape:",len(A[0]),len(A))
    for i in range(len(A[0])):
        #print("i:",i)
        for j in range(len(A)):
            #print("j:",j)
            B[i][j] = A[j][i]
    return B

def transpose_square(A):
    B = zeros(len(A),len(A))
    for i in range(len(A)):
        for j in range(len(A)):
            B[i][j] = A[j][i]
    return B

#perform matrix muliplication
def multiply(A,B):
    #check if col of A is equal to row of B
    if(len(B)!=len(A[0])):
        raise ValueError("COLUMN of first matrix must be EQUAL to the ROW of second matrix!")
    result_row = len(A)
    result_column = len(B[0])
    result = [[0 for i in range(result_column)]for j in range(result_row)]
    
    common_rowcol = len(B)
    #use traditional row times columns;
    #but other ways can perform this like MIT 16.04 Gilbert Strang
    for i in range(result_row):
        for j in range(result_column):
            for k in range(common_rowcol):
                result[i][j] += A[i][k]*B[k][j]
    
    return result

# matrix power, regular power see pow()
def power(A,k):

    if k != 0:
        k -= 1
        return multiply(power(A,k),A)
    if k == 0:
        return eyes(len(A))

#calculates the permutation of a set, used for calculating determinants
def permutation_sign(array):
    n = len(array)
    num = 0
    i,j = 0,1
    for i in range(n-1):
        for j in range(i+1,n):
            if array[i]>array[j]:
                num+=1
    #return num
    if is_even(num):
        return 1
    elif is_odd(num):
        return -1
#计算排列的逆序数，用于线性代数元素的符号判定
def permutation(array):
    n = len(array)
    num = 0
    i,j = 0,1
    for i in range(n-1):
        for j in range(i+1,n):
            if array[i]>array[j]:
                num+=1;
    return num
    
#返回一个数组的全排列，形式为二维数组，具体算法原理改日探讨
perm_num=0
perm_list = []
perm_count=0
# next time use perm, remember to reset the variables
def reset_perm(): # make a copy of the perm_list before reset
    global perm_num
    perm_num=0
    global perm_list
    perm_list = []
    global perm_count
    perm_count = 0

#用于生成给定元素的全排列
#每次递归调用一套perm生成全排列之前，手动调用一下reset_perm()，不然上次全排列的结果会遗留
"""
自己写的函数，代替方案是现成库函数
from itertools import combinations, permutations
print(list(permutations([1,2,3],3)))
"""
def perm(array, k, m): # For the 1st time, use directly without reset, 
                    # but do use for the next time, otherwise newly generated one appended to the original one
    global perm_list
    global perm_num
    global perm_count
    perm_count+=1
    
    #if(perm_count > factorial(len(array))):
        #pass#reset_perm()#想办法自动重置一下，但是找不到自动重置的时机，没有切入点
    if(k > m):
        perm_list.append([])
        #print("permutation",perm_num+1)
        for i in range(m+1):
            perm_list[perm_num].append(array[i])
            #print("%d  "%array[i],end='');
        #print("\n\n");
        perm_num+=1
 
    else:
        for i in range(k,m+1):
            array[k],array[i]=array[i],array[k]
            
            perm(array, k + 1, m);
            array[k],array[i]=array[i],array[k]
    
    return perm_list       
        

#calculates the determinant of the matrix
def det(A):
    '''
    there are several ways to calculate the determinant
    1.use permutations denote the sign and product of deferent rows and columns
    2.transform into upper triangular matrix, get the product of the diagonal
    3.expand determinant recursively
    '''
    #the third method is preferred as computer programs. 
    
    #method 1
    n = len(A) # 行数
    m = len(A[0]) # 列数
    if n!=m:
        raise ValueError("input NOT SQUARE matrix!")
    row = [i for i in range(n)] # 生成从0到n-1的列表，用于固定行标
    reset_perm()# 每次递归生成perm之前，手动清零一次
    col = perm(row,0,n-1)
    p = 1 # 用于每一小项累乘
    s = 0 # 行列式多项式求和
    for k in range(factorial(n)):
        #print("term",k+1)
        for (i,j) in transpose([row,col[k]]):   #这种来自不同行不同列的算法有点问题
            #print("item_",i,j)
            p*=A[i][j]
        s+=(permutation_sign(col[k])*p)
        p=1
        #print("permutation_sign:",permutation_sign(col[k]))

    return s


# diy a function like copy.deepcopy() 
def deepcopy(A):
    B = zeros(len(A),len(A[0]))
    for i in range(len(A)):
        for j in range(len(A[0])):
            B[i][j] = A[i][j]
    """
    C = A
    print(A,id(A),id(A[0]),id(A[0][0]))
    print(B,id(B),id(B[0]),id(B[0][0]))
    print(C,id(C),id(C[0]),id(C[0][0]))
    """
    return B
#import copy  #自己写一个deepcopy函数，这样就不用调用这唯一的库函数了
def minor(A,row,col):
    B = deepcopy(A) #如果直接复制，会把传进来的A给修改了 浅复制二维数组的每个元素指向的行向量是一个地址
    for i in range(len(B)):
        del B[i][col]
    del B[row]
    return (-1)**(row+col)*det(B)

# calculates the adjoint of a given matrix
def adjoint(A):    
    B = deepcopy(A)
    C = zeros(len(A),len(A[0]))
    row = len(A)
    col = len(A[0])
    for i in range(row):
        for j in range(col):
            C[i][j]=minor(B,j,i)

    return C
# calculates the inverse of a given matrix
def inv(A):
    B = adjoint(A)
    for i in range(len(B)):
        for j in range(len(B)):
            B[i][j]=B[i][j]/det(A)
    return B



#### functions below changes the original input matrix, copy if necessary ###
# exchange two certain rows of a given matrix
def exchange_rows(B,r1,r2):
    #B=deepcopy(A)
    B[r1],B[r2]=B[r2],B[r1]
    return B

# exchange two certain columns of a given matrix
def exchange_cols(B,c1,c2):
    #B=deepcopy(A)
    for i in range(len(B)):
        B[i][c1],B[i][c2]=B[i][c2],B[i][c1]
    return B

# multiply a certain row by a given factor
def multiply_row(B,r,k): # r the row number, k the factor
    for i in range(len(B[0])):
        B[r][i] = k*B[r][i]
    return B

def add_rows(B,r1,r2): # adds r2 to r1
    for i in range(len(B[0])):
        B[r1][i] += B[r2][i]
    return B


def add_rows_by_factor(B,r1,k,r2): # r1+k*r2, adds k*r2 to r1
    #r1-=1
    #r2-=1
    for i in range(len(B[0])):
        B[r1][i] += k*B[r2][i]
    return B

def add_rows_by_factor_approximate(B,r1,k,r2,appr = 10): # r1+k*r2 adds k*r2 to r1
    #r1-=1
    #r2-=1
    for i in range(len(B[0])):
        B[r1][i] = round(B[r1][i],appr)
        b = round(k*B[r2][i],appr)
        B[r1][i]+=b
    return B
################# end section ################    
# to form augmented matrix using this
# 改进：维数不同时可以自动填零
def comb_col(*matrices): #接受之后，matrices是一个三维列表   
    M = []
    for i in range(len(matrices[0])):
        M.append([])
    for k in range(len(matrices[0])):
        for i in range(len(matrices)):
            M[k].extend(matrices[i][k])
    return M
def comb_row(*matrices):
    M = []
    for k in range(len(matrices)):
        for i in range(len(matrices[k])):
            M.append(matrices[k][i])
    return M
def split_col(A):
    M = []
    for j in range(len(A[0])):
        N = []
        for i in range(len(A)):
            N.append([A[i][j]])
        M.append(N)
    return tuple(M)
def split_row(A):
    M = []
    for i in range(len(A)):
        M.append([A[i]])   # 把原来各自矩阵的一行转换成完整的二维矩阵
    return tuple(M) # 返回tuple,这样看起来像返回多个值，而不是三层list
#check i elements under a_ij is all zeros (a_ij included)
def below_all_zero(A,i,j):
    flag = 0
    for k in range(len(A)-i):
        if A[len(A)-k-1][j] == 0:
            flag+=0   
        
        else:
            flag+=1
    if flag>0:
        return False
    else:
        return True  
def 打印子式(A):
    from itertools import combinations
    rows = []
    for i in range(len(A)):
        rows.append(i)
    cols = []
    for i in range(len(A[0])):
        cols.append(i)
    n = min(len(A),len(A[0]))  
    while n>0:        
        new_rows =  list(combinations(rows,n))#包含了行所有的可能
        new_cols = list(combinations(cols,n))#包含了列所有的可能
        B = zeros(n,n)
        #print(new_rows)
        #print(new_cols)
        for a in range(len(new_rows)):
            for b in range(len(new_cols)):       
                for i in range(n):
                    for j in range(n):
                        B[i][j] = A[new_rows[a][i]][new_cols[b][j]]   
                print(B)
                #if det(B) != 0:
                    #return len(B)             
        n-=1
        #if n==0:
            #return 0
       
def rank(A):
    # convert to row echelon is complex, thus use direct calculation of the 最高阶非零子式
    from itertools import combinations
    rows = []
    for i in range(len(A)):
        rows.append(i)
    cols = []
    for i in range(len(A[0])):
        cols.append(i)
    n = min(len(A),len(A[0]))  
    while n>0:        
        new_rows =  list(combinations(rows,n))#包含了行所有的可能
        new_cols = list(combinations(cols,n))#包含了列所有的可能
        B = zeros(n,n)
        #print(new_rows)
        #print(new_cols)
        for a in range(len(new_rows)):
            for b in range(len(new_cols)):       
                for i in range(n):
                    for j in range(n):
                        B[i][j] = A[new_rows[a][i]][new_cols[b][j]]   
                #print_matrix(B,0)
                #print("det:",det(B))
                #print()
                #print()
                if det(B) != 0:
                    return len(B) 
                    #pass            
        n-=1
        if n==0:
            return 0
# modifies the original input matrix!
def approximate_matrix(A,appr = 10):
    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i][j] = round(A[i][j],appr)
    return A
### 有bug，问题在于python除法不太精确，所以需要自己写一个    
def row_echelon(M):
    # 写一个模拟人工化简矩阵的函数，可能超长
    #用递归试一下 
    # row,col 用于定位非零首元
    A = deepcopy(M)
    row = 0
    col = 0
    
    while row<len(A) and col<len(A[0]):
        if is_nonzero(A[row][col]):
            for i in range(row+1,len(A)):
                #add_rows_by_factor_approximate(A,i,-A[i][col]/A[row][col],row) # 这里精度限制在10位，计算 -A[i][col]/A[row][col] 时
                                                                               # 除法精度达不到要求 相加会消不掉，所以取一个能保证消掉的精度
                add_rows_by_factor(A,i,-A[i][col]/A[row][col],row)
                #print((row,col),i,"added:")
                #print_matrix(A,40)

            row += 1 #加到最后会溢出，不满足行列判断条件，跳出循环
            col += 1 #

        else:
            if below_all_zero(A,row,col):
                col+=1 #如果这个元素之下全都是0，就开始看下一列
            else:
                
                i,j = row,col
                while is_zero(A[i][j]) and i<len(A)-1:#
                    i+=1
                exchange_rows(A,row,i)

    return approximate_matrix(A,8)  # 精度上还是有问题，折衷之计


def row_echelon_display_process(M):
    # 写一个模拟人工化简矩阵的函数，可能超长
    #用递归试一下 
    # row,col 用于定位非零首元
    A = deepcopy(M)
    row = 0
    col = 0
    print("original matrix")
    print_matrix(A)
    while row<len(A) and col<len(A[0]):
        if is_nonzero(A[row][col]):
            for i in range(row+1,len(A)):
                #add_rows_by_factor_approximate(A,i,-A[i][col]/A[row][col],row) # 这里精度限制在10位，计算 -A[i][col]/A[row][col] 时
                k =  -A[i][col]/A[row][col]                                   # 除法精度达不到要求 相加会消不掉，所以取一个能保证消掉的精度
                add_rows_by_factor(A,i,k,row)
                if round(k,4) != 0:
                    print('r',i+1,"+(",round(k,4),")r",row+1)
                    print_matrix(A)

            row += 1 #加到最后会溢出，不满足行列判断条件，跳出循环
            col += 1 #

        else:
            if below_all_zero(A,row,col):
                col+=1 #如果这个元素之下全都是0，就开始看下一列
            else:
                
                i,j = row,col
                while is_zero(A[i][j]) and i<len(A)-1:#
                    i+=1
                exchange_rows(A,row,i)
                print("exchange r",row+1,"and r",i+1)
                print_matrix(A)
    return approximate_matrix(A,6)  # 精度上还是有问题，折衷之计

# 接收row_echelon的矩阵，找到pivot的位置，返回几个下标的tuple，在求rref时用得到
def find_pivot(A):

    '''
    print(A)
    print(row_echelon(A))
    print(A==row_echelon(A))
    if row_echelon(A)!=A:
        raise ValueError("input is not a Row Echelon!")
    '''
    #print_matrix(A)
    index_list = []
    for i in range(len(A)-1,0-1,-1):
        for j in range(len(A[0])):
            if A[i][j] == 0:
                continue
            else:
                index_list.append((i,j))
                break
    return index_list
def rref(A):
    B = row_echelon(A)
    index_list = find_pivot(B)
    for i in range(len(index_list)):
        multiply_row(B,index_list[i][0],1/B[index_list[i][0]][index_list[i][1]]) # 这里偶尔会出现除以0的错误，可以用随机阵暴力测试，需要继续研究原因
        for row in range(index_list[i][0]):
            #print(row)
            add_rows_by_factor(B,row,-B[row][index_list[i][0]],index_list[i][0])
            #print(-B[row][index_list[i][0]])
    return approximate_matrix(B,10)


# as for return value, the first index refers to num of rows; the second num of cols
def matrix_shape(A):
    return (len(A),len(A[0]))
# 等时机合适，引入矩阵对象，自带shape，维度，行列式，逆等特征

# raise error when infinite solutions
def solve_linear_equation(A,b):
    return multiply(inv(A),b)

def solve_augmented_mat(A):
    B = deepcopy(A)
    b = zeros(len(A),1)
    for i in range(len(A)):
        b[i][0] = A[i][len(A[0])-1]
        B[i].pop()

    return solve_linear_equation(B,b) 


# 区分无解（返回False），唯一解（返回解向量），无穷解（返回基础解系）
def solve_lineq_homo(A,print_ans = False):#这个暂时是齐次的，require一个系数矩阵
    #先判断解的类型
    if rank(A)<min(len(A),len(A[0])):   ##？？？如果是行数大于列数的情况呢？满秩也不过小于行数，这样一定是无穷解吗？
        # 有无穷多个解
        A = row_echelon(A)
        boundary = find_pivot(A)[0] # 最下面一个pivot，右边都是自由变量
        print(boundary)
        ans = nulls(min(len(A),len(A[0]))-rank(A)) # 基础解系的个数n-r(A)
        k=0
        for j in range(boundary[1]+1,len(A[0])):
            for i in range(len(A)):
                if i < boundary[0]+1:
                    ans[k].append([-A[i][j]])
                else:
                    if i == j:
                        ans[k].append([1])
                    else:
                        ans[k].append([0])
            k+=1
        if print_ans == True:
            for n in range(len(ans)):
                print_vector(ans[n],2)
        return tuple(ans)
        # 想想怎么依次取1，其余取0
        ###未完待续#####
    else:
        return zeros(len(A),1)


# 点积，自适应行向量and列向量
def dot(a,b,appr = 10):
    if matrix_shape(a)!=matrix_shape(b):
        raise ValueError("inputs should be VECTORS of SAME TYPE!")
    elif len(a)!= 1 and len(a[0])!= 1:
        raise ValueError("inputs should be VECTORS!")
    if len(a) == 1: # 说明是行向量
        s = 0
        for j in range(len(a[0])):
            s+=a[0][j]*b[0][j]
        return round(s,appr)
    if len(a[0])==1: # 说明是列向量
        s = 0
        for i in range(len(a)):
            s+=a[i][0]*b[i][0]
        return round(s,appr)
def matrix_add(A,B):
    if matrix_shape(A)!=matrix_shape(B):
        raise ValueError("inputs should be in SAME SHAPE!")
    C = zeros(len(A),len(A[0]))
    for i in range(len(A)):
        for j in range(len(A[0])):
            C[i][j] = A[i][j]+ B[i][j]
    return C
def matrix_minus(A,B):
    if matrix_shape(A)!=matrix_shape(B):
        raise ValueError("inputs should be in SAME SHAPE!")
    C = zeros(len(A),len(A[0]))
    for i in range(len(A)):
        for j in range(len(A[0])):
            C[i][j] = A[i][j]- B[i][j]
    return C
def times_const(k,A):
    C = zeros(len(A),len(A[0]))
    for i in range(len(A)):
        for j in range(len(A[0])):
            C[i][j] = k*A[i][j]
    return C
def norm(vec):
    if len(vec) == 1: # 说明是行向量
        s = 0
        for j in range(len(vec[0])):
            s+=vec[0][j]**2           
        return sqrt(s)
    if len(vec[0])==1: # 说明是列向量
        s = 0
        for i in range(len(vec)):
            s+=vec[i][0]**2
        return sqrt(s)
def unitize(vec):
    return times_const(1/norm(vec),vec)
# Gram Schmidt Orthogonalization 接收的是矩阵，一般来讲，向量组中向量的个数应等于向量的维数   
def schmidt_matrix(A):  #理论上来讲应该接收向量组
    if len(A)>len(A[0]):
        raise ValueError("num of vectors should be at least equal to the dimension of vectors! (make sure cols>=rows)")
    a = split_col(A)   # col_vec_group
    b =  zeros(len(A[0]),1) # orth_vec_group
    
    for i in range(len(a)):
        s = zeros(len(a),1)
        if i == 0:
            b[0] = a[0]
            b[0] = times_const(1/norm(b[0]),b[0])

        else:
            for j in range(0,i):
                s = matrix_add(times_const(dot(b[j],a[i])/dot(b[j],b[j]),b[j]),s) # 还得写一个矩阵对应元素相加
            b[i] = matrix_minus(a[i],s)             # 正交化
            #print_vector(b[i])
            #b[i] = times_const(1/norm(b[i]),b[i])   # 单位化
            b[i] = unitize(b[i])       # 单位化
    return tuple(b) # 返回向量组

# 剥一层tuple皮，然后把列向量转换成矩阵, 功能等同于comb_col, 但传入的是tuple, 传入一堆可变参数和传入一个tuple，效果是一样的
def grouptuple_2_matrix(vec_tuple):
    M = zeros(len(vec_tuple[0]),len(vec_tuple))
    for i in range(len(vec_tuple[0])):
        for j in range(len(vec_tuple)):
            M[i][j] = vec_tuple[j][i][0]          
    return M
def schmidt_vec_group(*vec):
    return schmidt_matrix(grouptuple_2_matrix(vec))
def is_lindependent(*vec):
    A = grouptuple_2_matrix(vec)
    if rank(A)<len(vec):
        return True
    else:
        return False
    #print_matrix(grouptuple_2_matrix(vec))
#自适应输入向量组和矩阵
def schmidt(*vecs_or_A):
    
    if len(vecs_or_A)==1:
        A = vecs_or_A[0]
        return schmidt_matrix(A)
    else:
        vecs = vecs_or_A
        return schmidt_matrix(grouptuple_2_matrix(vecs))

def is_orthogonal(A):
    vecs = split_col(A)
    #print_vector_group(vecs)
    for i in range(len(vecs)):
        for j in range(len(vecs)):
            if i!=j:
                if round(dot(vecs[i],vecs[j]),6)!=0: # 无理数精度原因误判，暴力测试出错率十万分之一
                    return False
    return True


def eigen_value(A):
    if check_matrix_square(A):
        import sympy # 不得已，用了sympy作符号计算，为解特征值
        λ = sympy.symbols("λ")
        E = eyes(len(A))
        S = matrix_add(A,times_const(-λ,E))
        #print(sympy.simplify(det(S)))
        return sympy.solve(det(S),λ)

    else:
        raise ValueError("input has to be SQUARE")
def eigen_polynomial(A):
    if check_matrix_square(A):
        import sympy # 不得已，用了sympy作符号计算，为解特征值
        λ = sympy.symbols("λ")
        E = eyes(len(A))
        S = matrix_add(A,times_const(-λ,E))
        return (sympy.factor(sympy.simplify(det(S))))
        

    else:
        raise ValueError("input has to be SQUARE")
def eigen_vector(A):

    val = eigen_value(A)
    E = eyes(len(A))
    for i in range(len(val)):
        S = matrix_add(A,times_const(-val[i],E))
        ##############这里回代矩阵已经有了，就差一个返回解向量的函数
        print(S)





if __name__ == "__main__":
    print_matrix([[1,2]])

    '''
    ###解线性方程组
    A = [[1,2,-1],
        [2,1,3],
        [-1,4,5]]
    b=[ [1],
        [7],
        [3]]
    #LU分解法
    L,U = lu(A)
    y = solve_linear_equation(L,b)
    print_vector(y)
    x = solve_linear_equation(U,y)
    print_vector(x)
    #增广矩阵法
    print_vector(solve_augmented_mat(comb_col(A,b)))
    '''

    '''
    ### 施密特正交化生成正交矩阵
    P = grouptuple_2_matrix(schmidt_matrix(A)) # 把正交向量组转成正交矩阵
    print(is_orthogonal(P))
    '''