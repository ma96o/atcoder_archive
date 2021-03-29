N = int(input())
xList = []
yList = []

for i in range(N):
    x, y = map(int, input().split())
    xList.append(x)
    yList.append(y)


count = 0

for i in range(N):
    x = xList[i]
    y = yList[i]
    for targetI in range(i+1, N):
        targetX = xList[targetI]
        targetY = yList[targetI]
        tilt = abs((y - targetY) / (x - targetX))
        if tilt >= -1 and tilt <= 1:
            count += 1


print(count)
