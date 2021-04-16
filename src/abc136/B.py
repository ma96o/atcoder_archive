n = int(input())
print(min(n, 9)+max(min(n-99, 900), 0)+max(min(n-9999, 90000), 0))

# for i in range(1, ln):
#     if n > 10*i:
#         ans = min(n, 9)


# if n < 100:  # 1 ~ 9 @10~99
#     ans = min(n, 9)
# elif n < 10000:  # 100 ~ 999 @1000 ~ 9999
#     ans = 9 + min(n-99, 900)
# elif n <= 100000:  # 10000 ~ 99999 @100000
#     ans = 9 + 900 + min(n-9999, 90000)

# print(ans)

# if n < 10:
#     ans = n
# elif n < 100:
#     ans = 9
# elif n < 1000:
#     ans = 9 + n - 99
# elif n < 10000:
#     ans = 9 + 900
# elif n < 100000:
#     ans = 9 + 900 + n - 999
# elif n == 100000:
#     ans = 9 + 900 + 90000

# print(ans)

# n = input()
# ln = len(n)
# if ln == 1:
#     ans = int(n)
# elif ln == 2:
#     ans = 9
# elif ln == 3:
#     ans = 9 + int(n) - 99
# elif len == 4:
#     ans = 9 + 900
# elif len == 5:
#     ans = 9 + 900 + int(n) - 999
# elif len == 6:
#     ans = 9 + 900 + 90000

# print(ans)
