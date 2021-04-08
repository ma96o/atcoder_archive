k = int(input())
s = input()

if len(s) <= k:
    print(s)
    exit()

print(s[:k], '...', sep='')
