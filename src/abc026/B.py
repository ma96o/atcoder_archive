import math
n = int(input())
rlist = [int(input()) for i in range(n)]
rlist.sort()
ans1 = 0
ans2 = 0
temp = 0

for i in range(n):
    r = rlist[i]
    area = math.pi * r * r
    if i % 2 == 0:
        ans1 += (area - temp)
    else:
        ans2 += (area - temp)
    temp = area


print(ans1 if n % 2 != 0 else ans2)
