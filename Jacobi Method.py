import numpy as np 


def jacobi(A,b,x):
    n = len(b)
    maxIt = 10000
    tol = 10**(-10)
    Dinv = np.zeros((n,n))
    L = np.zeros((n,n))
    U = np.zeros((n,n))
    for i in range(n):
        for j in range(n):
            if i == j:
                # we are on diagonal
                Dinv[i,j] = 1/A[i,j]
            elif i < j: 
                # we are on the upper triangular region
                U[i,j] = -A[i,j]
            else:
                # we are on the lower triangular region
                L[i,j] = -A[i,j]

    T = np.matmul(Dinv, L+U)
    c = np.matmul(Dinv,b)

    for i in range(maxIt):
        xnew = np.matmul(T,x) + c
        err = max(abs(xnew - x))
        if err <= tol:
            print( 'Solution is', xnew, 'after', i, 'iterations')
            return xnew
        elif  i == maxIt -1:
            print ('System did not converge')
            return []
        else:
            x = xnew
    print(xnew)


A = np.array([[5,-2,3], [-3,9,1],[2,-1,-7]])
b = np.array([-1,2,3])
n = len(b)
x = np.zeros(n)
jacobi(A,b,x)
