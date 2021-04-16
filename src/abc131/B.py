n, l = map(int, input().split())
tastes = list(abs(l+i) for i in range(n))
target_index = tastes.index(min(tastes))
print(l*(n-1) + n*(2+(n-1))//2 - (target_index + 1) - (n-1))

# tastes = []
# eat_i = 0
# target = abs(n+l-1)
# for i in range(n):
#     tastes.append(l+i)
#     x = abs(l+i)
#     if target > x:
#         target = x
#         eat_i = i


# print(sum(tastes[:eat_i]+tastes[(eat_i+1):]))
