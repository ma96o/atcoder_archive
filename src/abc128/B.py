import numpy as np
n = int(input())
slist = []
plist = []

for i in range(n):
    s, p = input().split()
    slist.append(s)
    plist.append(p)

indexes = np.argsort(slist)
lists = []
que = []
print(indexes)

for i in range(n):
    que.append(indexes[i])
    city = slist[indexes[i]]
    if i+1 == n:
        next_city = ''
    else:
        next_city = slist[indexes[i+1]]
    if city != next_city:
        lists.append(que)
        que = []

for l in lists:
    for i in l:
        plist[i]

print(lists)


n = int(input())
l = []

for i in range(n):
    s, p = input().split()
    l.append({s: int(p)})

print(ids)
