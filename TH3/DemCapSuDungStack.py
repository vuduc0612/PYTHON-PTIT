n = int(input())
ans = 0
st = []
cnt = {}
for i in range(1, n + 1):
    x = int(input())
    while st and x > st[-1]:
        cnt[st[-1]] -= 1
        st.pop()
        ans += 1
    if st:
        if x == st[-1]: ans += cnt[x] + (len(st) > cnt[x])
        else: ans += 1
    st.append(x)
    if x in cnt: cnt[x] += 1
    else: cnt[x] = 1
print(ans)