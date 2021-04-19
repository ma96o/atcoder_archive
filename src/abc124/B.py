n = int(input())
hlist = list(map(int, input().split()))

cnt = 0
maxh = 0
for h in hlist:
    if maxh <= h:
        cnt += 1
        maxh = h

print(cnt)
