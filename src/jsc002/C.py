import math
import itertools
import functools

a, b = map(int, input().split())
print(functools.reduce(math.gcd, list(range(a, b+1))))

gcds = []
for x, y in itertools.combinations(range(a, b+1), 2):
    gcds.append(math.gcd(x, y))

print(max(gcds))


u_list = range((a+b+1))


for i in range(b):
    target = b-i
    if target < a:
        break
    for j in range(1, target):
        target2 = target-j
        if target2 < a:
            break
        gcds.append(math.gcd(target, target2))


for x, y in itertools.combinations(range(a, b+1), 2):
    gcds.append(math.gcd(x, y))

print(max(gcds))


# print(itertools.combinations(range(a, b+1), 2))
