n, m = map(int, input().split())
alist = list(map(int, input().split()))
sa = sum(alist)
bl = sa / (m*4)

selects = list(filter(lambda a: a >= bl, alist))
print("Yes" if len(selects) >= m else "No")

# cnt = 0
# for i in range(n):
#     a = alist[i]
#     if a >= bl:
#         cnt += 1
#     if cnt == m:
#         print("Yes")
#         exit()
# print("No")

# a = sorted(list(map(int, input().split())), reverse=-1)
# if 4*m*a[m-1] < sum(a):
#     print("No")
# else:
#     print("Yes")
