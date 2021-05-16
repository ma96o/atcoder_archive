n = int(input())
tlist = list(map(int, input().split()))
m = int(input())
sumt = sum(tlist)
for i in range(m):
    p, x = map(int, input().split())
    print(sumt - tlist[p-1]+x)
