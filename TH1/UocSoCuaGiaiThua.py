t = int(input())
def count(n, p):
    cnt , mu = 0, p
    while p <= n:
        cnt += (n // p)
        p *= mu
    return cnt
for _ in range(t):
    n, p = map(int, input().split())
    print(count(n, p))