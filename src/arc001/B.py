a, b = map(int, input().split())
diff = abs(a-b)

ans = diff // 10 + (diff % 10) // 5 + (diff % 10) % 5

if diff % 10 == 8 or diff % 10 == 9:
    ans -= 1
if diff % 10 == 4 or diff % 10 == 9:
    ans -= 2

print(ans)
