n = int(input())
wlist = list(map(int, input().split()))

s1 = 0
s2 = sum(wlist)
ans = s2

for t in range(n):
    s1 += wlist[t]
    s2 -= wlist[t]
    diff = abs(s1 - s2)
    if ans >= diff:
        ans = diff
    else:
        break

print(ans)

# print(min(abs(sum(w[:i])-sum(w[i:]))for i in range(1, n)))
