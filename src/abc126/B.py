s = input()

front = int(s[:2])
behind = int(s[2:])

fmm = 1 <= front and front <= 12
bmm = behind >= 1 and behind <= 12

ans = "NA"

if fmm and bmm:
    ans = "AMBIGUOUS"
elif bmm:
    ans = "YYMM"
elif fmm:
    ans = "MMYY"

print(ans)
