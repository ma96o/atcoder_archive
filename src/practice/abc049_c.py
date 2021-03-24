S = input()

wordList = ["dream", "dreamer", "erase", "eraser", ""]
splitS = S.replace('d', ',d').replace('erase', ',erase').split(',')
incorrectList = list(filter(lambda str: not str in wordList, splitS))

print("YES" if len(incorrectList) == 0 else "NO")
