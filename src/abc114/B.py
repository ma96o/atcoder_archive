s = input()
diffs = []

for i in range(len(s)-2):
    bone = int(s[i]+s[i+1]+s[i+2])
    diff = abs(753-bone)
    diffs.append(diff)

print(min(diffs))
