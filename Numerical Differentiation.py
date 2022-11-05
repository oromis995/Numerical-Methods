import numpy as np 
import matplotlib.pyplot as plt 

h = 0.1
x = np.arange(0,2*np.pi+h,h)
f = np.sin(x)
n = len(x)

# Forward Difference
diffArr = np.diff(f)
backDiff = (f[n-1]-f[n-2])
fprime = np.append(diffArr,backDiff)
fprime = fprime/h
print('f',np.shape(f))
print('diffArr', np.shape(diffArr))

plt.plot(x,f)
plt.plot(x,fprime)
plt.grid()
plt.show()

