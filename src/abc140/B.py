n = int(input())
alist = list(map(int, input().split()))
blist = list(map(int, input().split()))
clist = list(map(int, input().split()))

sum = 0
prea = -1
for i in range(n):
    a = alist[i]
    sum += blist[a-1]
    if prea + 1 == a:
        sum += clist[prea-1]
    prea = a

print(sum)
