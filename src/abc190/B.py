N, S, D = map(int, input().split())
xList = []
yList = []

for i in range(N):
    x, y = map(int, input().split())
    xList.append(x)
    yList.append(y)

output = "No"

for i in range(N):
    x = xList[i]
    y = yList[i]
    if S > x and y > D:
        output = "Yes"
        break

print(output)
