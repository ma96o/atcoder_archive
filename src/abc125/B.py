n = int(input())
vlist = list(map(int, input().split()))
clist = list(map(int, input().split()))


ans = 0
for i in range(n):
    x = vlist[i]
    y = clist[i]
    ans += x-y if x-y > 0 else 0
    # ans += max(x-y, 0)


print(ans)


# print(sum(v-c for v,c in zip(*[[*map(int,input().split())] for _ in range(2)]) if v>c))
# print(sum(max(v-c, 0) for v, c in zip(vlist, clist)))
