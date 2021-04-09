n, k = map(int, input().split())
pList = list(map(int, input().split()))
pList.sort()

print(sum(pList[:k]))
