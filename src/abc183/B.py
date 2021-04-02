Sx, Sy, Gx, Gy = map(int, input().split())

tilt = (-Gy - Sy) / (Gx - Sx)
print(-Sy / tilt + Sx)

# y = tilt * x + hoge
# hoge = Sy - tilt * Sx
# outputX = - (Sy - tilt * Sx) / tilt
#         = - Sy / tilt + Sx
