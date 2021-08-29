def Euler(n):
    nr = n
    d = 2
    while d * d <= n:
        if n % d == 0:
            while n % d ==0:
                n //= d
            nr -= nr//d
        d = d + 1
    if n > 1:
        nr -= nr//n
    return nr



n=int(input())
print(Euler(n))