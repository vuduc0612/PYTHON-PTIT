from math import sqrt

M = 1000
class pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y
def mul(a, b):
    r = pair(0, 0)
    r.x = (a.x*b.x + 5*a.y*b.y)%M
    r.y = (a.x*b.y + a.y*b.x)%M
    return r
def powMod(a, b):
    if b == 0:
        return pair(1, 0)
    if b & 1:
        return mul(powMod(a, b - 1), a)
    p = powMod(a, b>>1)
    return mul(p, p)
x = pair(3, 1)
t = int(input())
for i in range(t):
    n = int(input())
    print(f'Case #{i + 1}:', end = ' ')
    print(str(powMod(x, n).x*2 % M -1).zfill(3))