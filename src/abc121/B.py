n, m, c = map(int, input().split())
blist = list(map(int, input().split()))

ans = 0

for i in range(n):
    alist = list(map(int, input().split()))
    if sum(a*b for a, b in zip(alist, blist)) > -c:
        ans += 1

print(ans)

# a = [[int(x) for x in input().split()] for _ in range(n)]
# print(sum(1 for a in a if sum(a*b for a, b in zip(a, blist)) > -c))
