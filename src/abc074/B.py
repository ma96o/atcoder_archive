n = int(input())
k = int(input())
xlist = map(int, input().split())

ans = 0
for x in xlist:
    ans += min(k-x, x)*2

print(ans)
