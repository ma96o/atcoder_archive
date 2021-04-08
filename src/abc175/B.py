import itertools

n = int(input())
ls = list(map(int, input().split()))
ls.sort()

cnt = 0
for combi in itertools.combinations(ls, 3):
    if len(combi) != len(set(combi)):
        continue
    a, b, c = combi
    if c < a+b:
        cnt += 1

print(cnt)
