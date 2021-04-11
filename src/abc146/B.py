n = int(input())
s = input()
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in range(len(s)):
    print(alpha[alpha.index(s[i])+n-26], end='')
