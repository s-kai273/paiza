N, X, Y = [int(x) for x in input().split()]

for i in range(1, N + 1):
    answer = ''
    if i % X == 0:
        answer += 'A'
    if i % Y == 0:
        answer += 'B'
    if answer == '':
        answer = 'N'
    print(answer)
