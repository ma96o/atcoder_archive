import itertools
N = input()

ans = -1
length = range(len(N))

if int(N) % 3 == 0:
    ans = 0
else:
    for i in range(1, len(N)):
        numsList = itertools.combinations(length, i)
        for nums in numsList:
            n = N
            cv = 0
            for num in nums:
                n = n[:num-cv] + n[num+1-cv:]
                cv += 1
            if int(n) % 3 == 0:
                ans = i
                break
        else:
            continue
        break

print(ans)
