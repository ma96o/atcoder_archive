r, x, y = map(int, input().split())

xy = int(pow(x, 2) + pow(y, 2))**0.5

ans = int(-(-xy//r)) if xy >= r else 2
print(ans)

# d = math.sqrt(x*x + y*y)
# if d == r:
#     print(1)
# elif d <= r+r:
#     print(2)
# else:
#     print(math.ceil(d/r))
