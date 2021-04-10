a1 = map(int, input().split())
a2 = map(int, input().split())
a3 = map(int, input().split())

n = int(input())
blist = []

for i in range(n):
    b = int(input())
    blist.append(b)

ja1 = list(map(lambda a: a in blist, a1))
ja2 = list(map(lambda a: a in blist, a2))
ja3 = list(map(lambda a: a in blist, a3))

j1 = not False in ja1 or not False in ja2 or not False in ja3
j2 = (ja1[0] and ja2[1] and ja3[2]) or (ja1[2] and ja2[1] and ja3[0])
j3 = False
for i in range(3):
    if ja1[i] and ja2[i] and ja3[i]:
        j3 = True
        break

if j1 or j2 or j3:
    print("Yes")
else:
    print("No")
