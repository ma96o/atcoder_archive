a, b = map(int, input().split())
s = input()
if s[a] == '-' and len(s) == a+b+1:
    for i in range(len(s)):
        if i == a:
            continue
        try:
            int(s[i])
        except ValueError:
            print("No")
            exit()
        else:
            continue
    print("Yes")
    exit()

print("No")
