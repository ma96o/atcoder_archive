n = int(input())
plist = []
for _ in range(n):
    p = int(input())
    plist.append(p)

print(sum(plist) - max(plist)//2)
