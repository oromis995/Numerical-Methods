

def horners(p0, P):

    n = len(P)
    Q = (n-1) * [0]
    #R = 0
    Q[0] = P[0]
    for i in range(1, n):
        if i == n - 1:
            R = Q[i-1] * p0 + P[i]
        else:
            Q[i] = Q[i-1] * p0 + P[i]
    print('Q', Q, 'R', R)
    return R, Q 

p0 = -2

P = [2, 0, -3, 3, -4]

[R,Q] = horners(p0, P) 