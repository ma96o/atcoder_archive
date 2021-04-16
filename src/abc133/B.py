import itertools

n, d = map(int, input().split())
xlist = []
ans = 0

for _ in range(n):
    xlist.append(list(map(int, input().split())))

for y, z in itertools.combinations(range(n), 2):
    ylist = xlist[y]
    zlist = xlist[z]
    sum = 0
    for i in range(d):
        sum += pow(ylist[i] - zlist[i], 2)
    if (sum**0.5).is_integer():
        ans += 1

print(ans)
