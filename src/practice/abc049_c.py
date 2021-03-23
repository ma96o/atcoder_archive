S = input()

S = S.replace('dreamere', 'e')
S = S.replace('dreamerd', 'd')
S = S.replace('dream', '')
S = S.replace('eraser', '')
S = S.replace('erase', '')

output = "YES" if len(S) == 0 else "NO"

print(output)
