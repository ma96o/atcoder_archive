import collections
n = int(input())
slist = [input() for i in range(n)]
cnts = collections.Counter(slist)

print('AC x ' + str(cnts['AC']))
print('WA x ' + str(cnts['WA']))
print('TLE x ' + str(cnts['TLE']))
print('RE x ' + str(cnts['RE']))
