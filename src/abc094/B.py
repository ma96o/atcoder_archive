n, m, x = map(int, input().split())
alist = set(map(int, input().split()))

first_half = set(range(x))
second_half = set(range(x+1, n+1))

print(min(len(first_half & alist), len(second_half & alist)))
