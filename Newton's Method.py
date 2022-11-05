import math as m

# DERIVATIVE APPROXIMATION AND THE SECANT METHOD
# If p_(n-2) is close to p_(n-1) then:
# f'(p_(n-1)) ~= [ f(p_(n-2)) -f(p_(n-1)) ] / p_(n-2) - p_(n-1) 


def f(x):
    # EDIT TO CHANGE FUNCTION
    return 2 * x**3 + x**2 - x + 1

def fPrime(x):
    # EDIT TO CHANGE FUNCTION
    return 6 * x**2 + 2 * x - 1

def NewtonsMethod(p):
    maxIt = 1000
    tolerance = 10**(-5)
    for i in range(maxIt):
        pNew = p - f(p)/fPrime(p)
        if m.fabs(p - pNew) < tolerance:
            p = pNew
            print('Iteration Number', i+1)
            return p
        elif i == maxIt - 1:
            print('Method Diverges')



        p = pNew
p0 = .1
root = NewtonsMethod(p0)
print(root)

