s = input()

ACGT = ['A', 'C', 'G', 'T']

ans = [0]
cnt = 0
for i in range(len(s)):
    if s[i] in ACGT:
        cnt += 1
    else:
        ans.append(cnt)
        cnt = 0

ans.append(cnt)
print(max(ans))
