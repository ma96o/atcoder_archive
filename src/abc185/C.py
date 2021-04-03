L = int(input())

up = 1
down = 1
for i in range(1, 12):
    up *= (L-i)
    down *= i


print(up//down)


# L = int(input())

# sum = 0
# left = 11
# count = 0
# for a1 in range(1, L - left + 1):
#     sum = a1
#     left = 10
#     for a2 in range(1, L - left - sum + 1):
#         sum = a1 + a2
#         left = 9
#         for a3 in range(1, L - left - sum + 1):
#             sum = a1 + a2 + a3
#             left = 8
#             for a4 in range(1, L - left - sum + 1):
#                 sum = a1 + a2 + a3 + a4
#                 left = 7
#                 for a5 in range(1, L - left - sum + 1):
#                     sum = a1 + a2 + a3 + a4 + a5
#                     left = 6
#                     for a6 in range(1, L - left - sum + 1):
#                         sum = a1 + a2 + a3 + a4 + a5 + a6
#                         left = 5
#                         for a7 in range(1, L - left - sum + 1):
#                             sum = a1 + a2 + a3 + a4 + a5 + a6 + a7
#                             left = 4
#                             for a8 in range(1, L - left - sum + 1):
#                                 sum = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8
#                                 left = 3
#                                 for a9 in range(1, L - left - sum + 1):
#                                     sum = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9
#                                     left = 2
#                                     for a10 in range(1, L - left - sum + 1):
#                                         sum = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10
#                                         left = 1
#                                         for a11 in range(1, L - left - sum + 1):
#                                             sum = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10 + a11
#                                             left = 0
#                                             count += 1

# L = int(input())

# count = 0
# init = 1
# for i in range(1, L - 10 + 1):
#     if init == 1:
#         sum = i
#         left = 10
#         init = 0
#     else:
#         sum += i
#         left -= 1
#     if L - left - sum <= 1:
#         continue
#     if left == 0:
#         count += 1
#         init = 1


# L = int(input())
# left = 11
# count = 0
# for a1 in range(1, L - left + 1):
#     sum1 = a1
#     left = 10
#     for a2 in range(1, L - left - sum1 + 1):
#         sum2 = sum1 + a2
#         left = 9
#         for a3 in range(1, L - left - sum2 + 1):
#             sum3 = sum2 + a3
#             left = 8
#             for a4 in range(1, L - left - sum3 + 1):
#                 sum4 = sum3 + a4
#                 left = 7
#                 for a5 in range(1, L - left - sum4 + 1):
#                     sum5 = sum4 + a5
#                     left = 6
#                     for a6 in range(1, L - left - sum5 + 1):
#                         sum6 = sum5 + a6
#                         left = 5
#                         for a7 in range(1, L - left - sum6 + 1):
#                             sum7 = sum6 + a7
#                             left = 4
#                             for a8 in range(1, L - left - sum7 + 1):
#                                 sum8 = sum7 + a8
#                                 left = 3
#                                 for a9 in range(1, L - left - sum8 + 1):
#                                     sum9 = sum8 + a9
#                                     left = 2
#                                     for a10 in range(1, L - left - sum9 + 1):
#                                         sum10 = sum9 + a10
#                                         left = 1
#                                         for a11 in range(1, L - left - sum10 + 1):
#                                             left = 0
#                                             count += 1


# print(count)
