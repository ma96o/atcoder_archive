a, b, c = map(int, input().split())
ans = '!'

if a+b == c:
    ans = '+'

if a-b == c:
    if ans == '+':
        ans = '?'
    else:
        ans = '-'

print(ans)
