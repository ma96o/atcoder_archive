n = int(input())
t, a = map(int, input().split())
hlist = [map(int, input().split())]
diffs = []

for i in range(n):
    h = hlist[i]
    diff = abs(a-(t-h*0.006))
    diffs.append(diff)
