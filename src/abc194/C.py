# import numpy as np

N = int(input())
aList = list(map(int, input().split()))

SUM1 = 0
SUM2 = 0
SUM3 = 0

for a in aList:
    SUM1 += a**2
    SUM2 += a * SUM3
    SUM3 += a

SUM = (N - 1) * SUM1 - 2 * SUM2
print(SUM)


# ↓proto
# SUM = sum(map(lambda i, v: (N - 1) * v ** 2 - 2 *
#           v * int(sum(aList[:i])), range(N), aList))
# print(SUM)

# SUM = 0
# for i in range(0, N):
#     SUM += (N - 1) * aList[i]**2 - 2 * \
#         aList[i] * int(sum(aList[:i]))
# print(SUM)


# SUM = 0
# SUM += (N - 1) * sum(map(lambda v: v ** 2, aList))
# for i in range(1, N):
#     SUM -= 2 * aList[i] * int(sum(aList[:i]))
# print(SUM)

# SUM = 0
# SUM += (N - 1) * sum(np.power(aList, 2))
# for i in range(1, N):
#     SUM -= 2 * aList[i] * int(sum(aList[:i]))
# print(SUM)


# SUM = (N - 1) * aList[N - 1]**2
# for i in range(0, N-1):
#     SUM += (N - 1) * aList[i]**2 - 2 * \
#         aList[i + 1] * int(sum(aList[:i+1]))
# print(SUM)


# sum = 0
# for i in range(2, N + 1):
#     for j in range(1, i):
#         diff = aList[i - 1] - aList[j - 1]
#         sum += diff ** 2

# sum = 0
# for x in range(1, N):
#     for y in range(x + 1, N + 1):
#         diff = aList[y - 1] - aList[x - 1]
#         sum += diff ** 2


# https://atcoder.jp/contests/abc194/submissions/21216471
# N = int(input())
# A = list(map(int, input().split()))
# ans1 = 0
# ans2 = 0
# for i in range(0, N):
#     ans1 += A[i] ** 2
#     ans2 += A[i]
# ans = N * ans1 - ans2 ** 2
# print(ans)


# https://atcoder.jp/contests/abc194/submissions/20702693
# n=int(input())
# k=map(int,input().split())
# p=0
# q=0
# for a in k:
#     p+=a**2*(n-1)
#     p-=2*q*a
#     q+=a
# print(p)
