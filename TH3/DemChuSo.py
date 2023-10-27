def f(x, n):
    res = 0
    for i in range(10):
        m = 10**i 
        if m > n: break 
        a = n // m 
        b = n % m
        c = a % 10
        if c > x: 
            res += ((a//10) + 1) * m 
        elif c == x: 
            res += (a//10) * m + (b + 1)
        else: 
            res += (a//10)*m 
        if x == 0: res -= m
    return res

def Count(d, l, r):
    return f(d, r) - f(d, l - 1)

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    for i in range(10):
        print(Count(i, a, b), end = ' ')
    print()