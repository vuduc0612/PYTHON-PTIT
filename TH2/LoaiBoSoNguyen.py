def check(s):
	for x in s:
		if not x.isdigit():
			return False
	return len(s) > 9
def check2(s):
	dem = 0
	for x in s:
		if x.isalpha():
			dem += 1
	return dem > 0
f = open("DATA.in", "r")
a = []
for x in f.read().split():
	if check2(x) or check(x):
		a.append(x)
a.sort()
for x in a:
	print(x, end = ' ')
