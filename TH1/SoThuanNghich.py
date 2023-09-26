def check(num, m):
    tmp = ""
    while num:
        tmp += str(num % m)
        num //= m
    return tmp == tmp[::-1]
def check_bin(n):
    tmp = bin(n)[2:]
    return tmp == tmp[::-1]
a, b, m = map(int, input().split())
ans = [x for x in range(a, b + 1) if check_bin(x)]
print(ans)
for cs in range(2, m + 1):
    tmp = [x for x in ans if check(x, cs)]
    print(tmp)
    if len(tmp) == 0: break
print(len(tmp))