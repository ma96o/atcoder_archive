n = int(input())
t, a = map(int, input().split())
hlist = list(map(int, input().split()))
ans = 0
temp = 10**5

for i in range(n):
    h = hlist[i]
    diff = abs((t-h*0.006)-a)
    if diff < temp:
        temp = diff
        ans = i+1

print(ans)
