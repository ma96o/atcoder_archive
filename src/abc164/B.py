import math
a, b, c, d = map(int, input().split())

if math.ceil(a / d) >= math.ceil(c / b):
    print("Yes")
else:
    print("No")


# t = True
# while a > 0 and c > 0:
#     if t:
#         c -= b
#     else:
#         a -= d
#     t = not t

# print("Yes" if not t else "No")
