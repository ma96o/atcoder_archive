S = input()
T = input()

tlen = len(T)

cnt = 0
maxCnt = 0
for i in range(tlen):
    t = T[i]
    if t in S[i:]:
        cnt += 1
        maxCnt = max(maxCnt, cnt)
    else:
        count = 0


print(tlen-maxCnt)


ans = 0
for i in range(tlen):
    if T[:tlen-i] in S or T[i:] in S:
        ans = i
        break
