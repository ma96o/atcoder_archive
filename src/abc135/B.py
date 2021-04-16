n = int(input())
plist = list(map(int, input().split()))
splist = sorted(plist)

cnt = 0
for i in range(n):
    if plist[i] != splist[i]:
        cnt += 1


print("YES" if cnt <= 2 else "NO")
