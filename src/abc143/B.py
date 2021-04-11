n = int(input())
dlist = list(map(int, input().split()))

sum = 0
for i in range(n):
    x = dlist[i]
    for j in range(i+1, n):
        y = dlist[j]
        sum += x*y

print(sum)
