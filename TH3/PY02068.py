t = int(input())
while t > 0:
	n, m, k = map(int, input().split())
	a = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
	for i in range(1, n + 1):
		a[i] = [0] + list(map(int, input().split()))
	prefix = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
	for i in range(1, n + 1):
		for j in range(1, m + 1):
			prefix[i][j] = prefix[i][j - 1] + prefix[i - 1][j] - prefix[i - 1][j - 1] + a[i][j]
	const = k * k
	for i in range(1, n - k + 2):
		for j in range(1, m - k + 2):
			res = prefix[i + k - 1][j + k - 1] -  prefix[i - 1][j + k - 1] - prefix[i + k - 1][j - 1] + prefix[i - 1][j - 1]
			print(res//const, end = ' ')
		print()
	t -= 1
