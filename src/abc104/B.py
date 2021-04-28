s = input()

print("AC" if s[0] == "A" and s.count("C", 2, -1) ==
      1 and s.replace("A", "").replace("C", "").islower() else "WA")
