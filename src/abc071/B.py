s = input()

alpha = 'abcdefghifklmnopqrstuvwxyz'

for a in alpha:
    if not a in s:
        print(a)
        exit()

print('None')
