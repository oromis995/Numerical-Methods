# Write a function that uses Steffensen's Method to approximate
# the root of a mathematical function. Use Steffensen's Method
# to find the root of x - 2^-x = 0 that lies in the interval
# [0,1] with accuracy of 10^-4

# default left and right bounds of interval
a = 0
b = 1

# our default function
def f(x):
    return x - 2**(-x)

def Steffensen(leftBound, rightBound, maxIterations):

    for i in range(0, maxIterations):
        # find the point in the center of the interval for x_0
        if i == 0:
            x = (a+b)/2
            print('x_'+str(0) +': ',x)
        # f(x_0)
        l1 = f(x)
        print("f(x_0) = " + str(round(l1,4)))
        # f(x_0 + f(x_0))
        l2 = f(x + f(x))
        print("f(x_0 + f(x_0)) = " + str(round(l2,4)))
        # our new x value
        oldx = x
        x = round(x - (l1**2)/(l2-l1),4)
        print('x_'+str(i+1) +': ',x)
        # early exit condition for lower processing
        if oldx == x:
            print("converged on iteration "+ str(i) + ", exiting before maxIts")
            break



Steffensen(a,b,5)