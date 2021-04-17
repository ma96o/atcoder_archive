n, m = map(int, input().split())
alist = list(map(int, input().split()))
blist = list(map(int, input().split()))

ans = []

for i in range(n):
    a = alist[i]
    if a in blist:
        continue
    ans.append(a)

for i in range(m):
    b = blist[i]
    if b in alist:
        continue
    ans.append(b)

print(*sorted(ans))
