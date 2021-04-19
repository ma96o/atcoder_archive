import math
l = [int(input()) for _ in range(5)]
ans = sum([math.ceil(x/10)*10 for x in l])
l2 = [x % 10 for x in l if x % 10 != 0]
last = 10 - min(l2) if len(l2) != 0 else 0
print(ans - last)


# print(l)
# print([math.ceil(x/10)*10 for x in l])
# print(ans)
# print([x % 10 for x in l if x % 10 != 0])
