s = input()

alpha = 'abcdefghifklmnopqrstuvwxyz'
# alpha = [chr(i) for i in range(97, 123)]

for a in alpha:
    if not a in s:
        print(a)
        exit()

# for i in range(97, 97+26):
# for i in range(ord('a'), ord('z')+1):
#     if chr(i) not in s:
#         print(chr(i))
#         exit()

print('None')
