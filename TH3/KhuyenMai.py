from functools import cmp_to_key


n, k = map(int, input().split())
b = []
c = []
b = list(map(int, input().split()))
c = list(map(int, input().split()))
a = []
for i in range(n):
	tmp = [] + [b[i]] + [c[i]]
	a.append(tmp)

a.sort(key = lambda x : (x[0] - x[1], x[1]))
#print(a)
ans = 0
for i in range(k):
	ans += a[i][0]
	#print(a[i][0])
for i in range(k, n):
	ans += min(a[i][0], a[i][1])
print(ans)
