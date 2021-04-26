n = int(input())
words = []
temp = ''

for i in range(n):
    w = input()
    if (len(temp) != 0 and temp[-1] != w[0]) or w in words:
        print("No")
        exit()
    words.append(w)
    temp = w

print("Yes")
