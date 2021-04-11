a, b, k = map(int, input().split())
print(max(a-k, 0), min(max(b-k+a, 0), b))

# for _ in range(k):
#     if a > 0:
#         a -= 1
#     elif b > 0:
#         b -= 1

# print(a, b)
