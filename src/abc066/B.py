s = input()
l = len(s)

for i in range(2, l)[::2]:
    s, l = s[:-2], l-2
    if s[:l//2] == s[l//2:]:
        print(l)
        exit()

s = input()[:-2]
while s[:len(s)//2] != s[len(s)//2:]:
    s = s[:-2]
print(len(s))
