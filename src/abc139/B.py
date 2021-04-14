a, b = map(int, input().split())
print(-(-(b-1) // (a-1)))


# ↓なぜこうなるかわかってない
# print((b+a-3)//(a-1))
