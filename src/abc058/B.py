o = input()
e = input()
# e = input() + ' '

for i in range(len(o)-1):
    print(o[i]+e[i], end='')

print(o[-1]+e[-1] if len(e) == len(o) else o[-1])
