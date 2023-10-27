from collections import deque
adj = [[] for _ in range(100005)]
deg = [0]*100005
idx = 1
d = dict({})
def kahn():
    q = deque()
    for i in range(1, idx + 1):
        if deg[i] == 0:
            q.append(i)
    cnt = 0
    while q:
        v = q.popleft()
        cnt += 1
        for x in adj[v]:
            deg[x] -= 1
            if deg[x] == 0: q.append(x)
    if cnt < idx: return True
    else: return False
for _ in range(int(input())):
    s1, s2, s3 = input().split()

    if s1 not in d:
        d[s1] = idx
        idx += 1
    if s3 not in d:
        d[s3] = idx
        idx += 1
    if s2 == ">":
        adj[d[s1]].append(d[s3])
        deg[d[s3]] += 1
    else:
        adj[d[s3]].append(d[s1])
        deg[d[s1]] += 1
idx -= 1
if kahn():
    print("impossible")
else:
    print("possible")