t = int(input())
def count(a, n):
    st1, st2 = [], []
    b, c = [0]*n, [0]*n
    for i in range(n - 1, -1, -1):
        while len(st1) > 0 and a[i] <= a[st1[-1]]: st1.pop()
        if len(st1) == 0: b[i] = -1
        else: b[i] = st1[-1]
        st1.append(i)
    for i in range(n):
        while len(st2)  > 0 and a[i] >= a[st2[-1]]: st2.pop()
        if len(st2) == 0: c[i] = -1
        else: c[i] = st2[-1]
        st2.append(i)
    cnt, d = 0, {}
    for i in range(n):
        if b[i] == -1 and c[i] == -1 and not a[i] in d:
            cnt += 1
            d[a[i]] = 1
    return cnt 

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(count(a, n))
