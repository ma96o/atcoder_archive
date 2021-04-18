n = int(input())
vlist = list(map(int, input().split()))
clist = list(map(int, input().split()))

ans = 0
for i in range(n):
    x = vlist[i]
    y = clist[i]
    ans += x-y if x-y > 0 else 0

print(ans)
