import itertools
n = int(input())
alist = list(map(int, input().split()))

cnt = 0
for x, y in itertools.combinations(range(n), 2):
    if (alist[x] - alist[y]) % 200 == 0:
        cnt += 1

print(cnt)
