N = int(input())
sList = [input() for i in range(N)]

withoutExS = []
withExS = []
output = 'satisfiable'


def distribute(x):
    if x[0] == '!':
        withExS.append(x.replace('!', ''))
    else:
        withoutExS.append(x)


list(map(distribute, sList))
dublicates = list(set(withExS) & set(withoutExS))
if len(dublicates) != 0:
    output = dublicates[0]

print(output)


# for str in withExS:
#     str = str
#     if str in withoutExS:
#         output = str
#         break
