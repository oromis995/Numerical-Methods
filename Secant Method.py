import math as m


def f(x):
    # EDIT TO CHANGE FUNCTION
    return 2 * x**3 + x**2 - x + 1



def SecantMethod(p0, p1):
    maxIt = 1000
    tolerance = 10**(-5)
    for i in range(maxIt):
        fp0 = f(p0)
        fp1 = f(p1)
        pNew = p1 - fp1*(p1-p0)/(fp1-fp0)
        
        if m.fabs(p1 - pNew) < tolerance:
            p = pNew
            print('Iteration Number', i+1)
            return p
        elif i == maxIt - 1:
            print('Method Diverges')


        p0 = p1
        p1 = pNew
p0 = -1.2
p1 = -1.3
root = SecantMethod(p0, p1)
print(root)

