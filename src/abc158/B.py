n, a, b = map(int, input().split())

ans = (n // (a+b))*a
l = n % (a+b)

if l >= a:
    ans += a
else:
    ans += l

print(ans)


print((n // (a+b))*a + min(l, a))
