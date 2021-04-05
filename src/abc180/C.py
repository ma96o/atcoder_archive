N = int(input())

lower_ans, upper_ans = [], []
i = 1

while i*i <= N:
    if N % i == 0:
        lower_ans.append(i)
        if i*i != N:
            upper_ans.append(N//i)
    i += 1

print(*(lower_ans + upper_ans[::-1]), sep='\n')
