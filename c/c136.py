N = int(input())
x_list = [int(input()) for _ in range(N)]

max_do_diet = 0
max_neglect = 0

successive_count = 0
prev_x = None
for i in range(N):
    x = x_list[i]
    if i == 0:
        prev_x = x
        continue

    if successive_count >= 0 and x < prev_x:
        successive_count += 1

    elif successive_count <= 0 and x > prev_x:
        successive_count -= 1

    else:
        if successive_count > 0:
            if successive_count > max_do_diet:
                max_do_diet = successive_count
            successive_count = -1
        elif successive_count < 0:
            if successive_count * -1 > max_neglect:
                max_neglect = successive_count * -1
            successive_count = 1

    prev_x = x

if successive_count > max_do_diet:
    max_do_diet = successive_count
elif successive_count * -1 > max_neglect:
    max_neglect = successive_count * -1

print('{} {}'.format(max_do_diet, max_neglect))
