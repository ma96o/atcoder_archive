import math
n = int(input())
alist = map(int, input().split())
all, cnt = [0, 0]

for a in alist:
    if a > 0:
        cnt += 1
        all += a

print(math.ceil(all/cnt))
