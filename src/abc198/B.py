n = input()
ln = len(n)

vn = n

if vn[-1] != '0':
    if ln % 2 == 0:
        if vn[:(ln // 2)] == vn[(ln // 2):][::-1]:
            print("Yes")
            exit()
    elif vn[:((ln-1)//2)] == vn[((ln+1)//2):][::-1]:
        print("Yes")
        exit()
    print("No")
    exit()

lvn = ln
for i in range(ln):
    vn = '0' + vn
    lvn += 1
    if lvn % 2 == 0:
        if vn[:(lvn // 2)] == vn[(lvn // 2):][::-1]:
            print("Yes")
            exit()
    elif vn[:((lvn-1)//2)] == vn[((lvn+1)//2):][::-1]:
        print("Yes")
        exit()

print("No")
