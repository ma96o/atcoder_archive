n = int(input())
s = input()
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in range(len(s)):
    print(alpha[alpha.index(s[i])+n-26], end='')

# ans = ''
# for s in S:
#     ans += chr(ord('A') + (ord(s)-ord('A')+n) % 26)

# print(ans)
