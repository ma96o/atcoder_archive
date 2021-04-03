import itertools
N, K = map(int, input().split())
tLists = [list(map(int, input().split())) for i in range(N)]

nums = list(range(1, N))
ans = 0

for index in itertools.permutations(nums):
    index = [0]+list(index)+[0]
    sum = 0
    for i in range(N):
        sum += tLists[index[i]][index[i+1]]
    if sum == K:
        ans += 1

print(ans)

# for a1 in range(1, N):
#     sum = tLists[0][a1]
#     if N == 2:
#         sum += tLists[a1][0]
#         print('sum2', sum)
#         if sum == K:
#             count += 1
#         continue
#     for a2 in range(1, N):
#         sum += tLists[a1][a2]
#         if N == 3:
#             sum += tLists[a2][0]
#             print('sum3', sum)
#             if sum == K:
#                 count += 1
#             continue
#         for a3 in range(1, N):
#             sum += tLists[a2][a3]
#             print('sum4', sum)
#             if N == 4:
#                 sum += tLists[a2][0]
#                 if sum == K:
#                     count += 1
#                 continue

# print(count)

# for i in range(N):
#     tList = tLists[i]

# for j in range(N):


# for i in range(N):
#     [map(int, input().split())]


# N = 4
# a = []
# for i in range(2, N-1):
#     a[0] = 1
#     for j in range(1, N-1):
#         a[j] = i
