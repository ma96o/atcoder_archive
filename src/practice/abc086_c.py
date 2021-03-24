N = int(input())
tList = []
xList = []
yList = []
for i in range(N):
    t, x, y = map(int, input().split())
    tList.append(t)
    xList.append(x)
    yList.append(y)


output = "Yes"
preT = 0
preS = 0

for n in range(N):
    x = xList[n]
    y = yList[n]
    t = tList[n]
    s = x + y
    delT = t - preT
    if not s in list(map(lambda i: preS + (delT - 2 * i), range(delT + 1))):
        output = "No"
        break
    preT = t
    preS = s


print(output)
