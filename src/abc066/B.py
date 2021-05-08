s = input()
l = len(s)

for i in range(2, l)[::2]:
    s, l = s[:-2], l-2
    if s[:l//2] == s[l//2:]:
        print(l)
        exit()
