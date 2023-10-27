t = int(input())
for _ in range(t):
	n = int(input())
	a, b = [], []
	f = [1]*n 
	for i in range(n):
		x, y = map(float, input().split())
		a.append(x)
		b.append(y)
	for i in range(n):
		for j in range(i):
			if a[j] < a[i] and b[j] > b[i]:
				f[i] = max(f[i], f[i] + 1)
	print(max(f))