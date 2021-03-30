H, W = map(int, input().split())
aList = []
for i in range(H):
    aList.extend([int(j) for j in input().split()])

count = 0
minA = min(aList)

for a in aList:
    diff = a - minA
    count += diff

print(count)
