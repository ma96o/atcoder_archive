from collections import Counter
n = int(input())
alist = Counter(list(map(int, input().split())))
blist = list(map(int, input().split()))
clist = Counter(list(map(int, input().split())))

cnt = 0
for v, c in clist.items():
    cnt += alist[blist[v-1]]*c

print(cnt)
