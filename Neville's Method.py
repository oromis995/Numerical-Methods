import numpy as numpy


def neville(x, y, xr):
    n = len(x)
    Q = np.zeros([n,n])
    Q[:,0] = y
    for i in range(1,n):
        for j in range(1, i+1):
            Q[i,j] = ((xr - x[i-j])*Q[i,j-1]) - (xr -x[i])*Q[i-1,j-1]
    return Q 

xr = 8.4
x = [8.1, 8.3, 8.6, 8.7]
y = [16.9, 17.6, 18.5, 18.8]

O = neville(x, y, xr)