import collections

n = int(input())
blist = collections.Counter(list(input() for _ in range(n)))
m = int(input())
rlist = collections.Counter(list(input() for _ in range(m)))

ans = 0
for b in blist.keys():
    ans = max(blist[b] - rlist[b], ans)

print(ans)


# print(max([s.count(k)-t.count(k) for k in s]+[0]))
