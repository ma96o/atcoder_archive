s = input()

front = int(s[:2])
behind = int(s[2:])

fmm = 1 <= front and front <= 12
bmm = behind >= 1 and behind <= 12

# fmm = 1 <= front <= 12
# fmm = 1 <= behind <= 12

ans = "NA"

if fmm and bmm:
    ans = "AMBIGUOUS"
elif bmm:
    ans = "YYMM"
elif fmm:
    ans = "MMYY"

print(ans)


# print(["NA","YYMM", "MMYY", "AMBIGUOUS"][2*(0<s//100<13)+(0<a%100<13)])
