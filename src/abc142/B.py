n, k = map(int, input().split())
hlist = list(map(int, input().split()))
print(len(list(filter(lambda h: h >= k, hlist))))
