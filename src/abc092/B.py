n = int(input())
d, x = map(int, input().split())

ans = x
for _ in range(n):
    a = int(input())
    ans -= (-d)//a

print(ans)
