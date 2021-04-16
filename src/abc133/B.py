n = int(input())
plist = list(map(int, input().split()))

ans = 0
for i in range(n-2):
    p1 = plist[i]
    p2 = plist[i+1]
    p3 = plist[i+2]
    if (p2 <= p1 and p2 > p3) or (p2 > p1 and p2 <= p3):
        ans += 1

print(ans)
