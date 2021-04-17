n, x = map(int, input().split())
l = list(map(int, input().split()))

ans = 1
d = 0

for i in range(n):
    d += l[i]
    if d > x:
        break
    ans += 1

print(ans)
