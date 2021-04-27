h, w = map(int, input().split())

ans = []
judge = [False for i in range(w)]

for i in range(h):
    inp = input()
    for j in range(w):
        if inp[j] == '#':
            judge[j] = True
    if '#' in inp:
        ans.append(inp)

for k in range(len(ans)):
    alist = ans[k]
    for l in range(w):
        if judge[l]:
            print(alist[l], end='')
    print('')
