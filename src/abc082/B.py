S = sorted(input())
T = sorted(input(), reverse=True)
# print("Yes" if S < T else "No")

s_s, t_s = '', ''

for s in S:
    s_s += s

for t in T:
    t_s += t

print("Yes" if s_s < t_s else "No")
