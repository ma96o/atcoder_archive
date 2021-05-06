h, w = map(int, input().split())
slists = list(input() for _ in range(h))

for i in h:
    target_lists = [slists[i]]
    if i > 0:
        target_lists.append(slists[i-1])
    elif i < h-1:
        target_lists.append(slists[i+1])
    for j in range(w):
        if slists[i][j] == '#':
            continue
        count = 0
        target_lists
        targets = [
            slist[j-1],
            slist[j],
            slist[j+1],
        ]
        count = targets.count('#')

        slist[j] = count


print(*slists, sep='\n')
