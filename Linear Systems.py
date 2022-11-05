from scipy.linalg import inv
import numpy as np

A = np.array([[1,-1,2,-1],[2,-2,3,-3],[1,1,1,0],[1,-1,4,3]])
b = np.array([[-8],[-20],[-2],[4]])
x = inv(A).dot(b)
print(x)