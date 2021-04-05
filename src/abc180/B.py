import math
N = int(input())
xList = list(map(int, input().split()))

ans1 = 0
ans2 = 0
ans3 = 0

for i in range(N):
    x = abs(xList[i])
    ans1 += x
    ans2 += x ** 2
    if ans3 < x:
        ans3 = x

print(ans1, math.sqrt(ans2), ans3, sep='\n')
