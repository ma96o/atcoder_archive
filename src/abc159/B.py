s = input()
n = len(s)

hs = s[:(n-1)//2]
vs = s[((n+3)//2-1):]

if s == s[::-1] and hs == hs[::-1] and vs == vs[::-1]:
    print("Yes")
    exit()

print("No")
