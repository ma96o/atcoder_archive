k, x = map(int, input().split())

ans = []
min_num = max((x-k+1), -1000000)
max_num = min((x+k-1), 1000000)

d_num = min_num
u_num = max_num
for _ in range(k):
    if not d_num in ans:
        ans.append(d_num)
    if not u_num in ans:
        ans.append(u_num)
    d_num += 1
    u_num -= 1

print(*sorted(ans))
