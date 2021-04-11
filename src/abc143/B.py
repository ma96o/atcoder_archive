n = int(input())
dlist = list(map(int, input().split()))

sum = 0
for i in range(n):
    x = dlist[i]
    for j in range(i+1, n):
        y = dlist[j]
        sum += x*y

print(sum)

# d_paires = itertools.combinations(dlist, 2)
# for i in d_paires:
#     sum += i[0]*i[1]

print(sum(d*c for d, c in zip(dlist[1:], itertools.accumulate(dlist))))
