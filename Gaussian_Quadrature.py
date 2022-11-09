
def gauss_points(n):

    if n == 2:

        c = [1,1]
        r = [0.5773502692, -.5773502692]

        return (c,r)

    elif n == 3:

        c = [.55555555, .888888888, .55555555]
        r = [.7745966692, 0, -.7745966692]

        return (c,r)

    elif n == 4:
        
        c = [0.34785485,0.65214515,0.65214515,
                0.34785485]
                
        r = [0.86113631,0.33998104,-0.33998104,
                -0.86113631]
        
        return (c,r) 

    elif n == 5:

        c = [0.2369268850,0.4786286705,0.5688888889,
                0.4786286705,0.2369268850]
        r = [0.9061798459,0.5384693101,0.000000000,
                -0.5384693101,-0.9061798459]
        
        return (c,r)

    else:

        print('Value not supported.')

def f(x):

    return x**2


n = 5
a = 0
b = 1


[c,r] = gauss_points(n)

area = 0 #initialize area


# Part of the Integral that can be pulled out
# will be called multiplier

multiplier = ((b-a)/2)



for i in range(n):
    
    area += (c[i]*f(((b-a)*r[i]+b+a)/2))
    print("iteration", i, "area", area)

area = area*multiplier

print("final value:", area)