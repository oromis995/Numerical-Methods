def gauss_points(n):
    if n == 2:
        c = [1,1]
        r = [0.6773502692, -0.6773502692]
        return (c,r)
    
    if n == 3:
        c = [0.55555555, 0.88888888, 0.55555555]
        r = [0.7745966692, 0, -0.7745966692]
        return (c,r)
    else:
        print ("value not supported.")

def f(x):
    exit

def transformed_f(x):
    exit


n = 2
[c,r] = gauss_points(n)
print(c)
print(r)

for i in range(n):
    #sum of c_i * f(x_i):
    exit