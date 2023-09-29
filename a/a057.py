N = int(input())
s_list = list()

for _ in range(N):
    s = input()
    s_list.append([int(c) for c in list(s)])


def swipe_count(i, j, dx, dy):
    if i + dx < 0 or i + dx > len(s_list[0]) - 1 or \
       j + dy < 0 or j + dy > len(s_list) - 1:
        return 0

    d = s_list[i][j] - s_list[i+dx][j+dy]
    if d == 1 or d == -1:
        return swipe_count(i+dx, j+dy, dx, dy) + 1
    else:
        return 0


max_count = 0
for i in range(len(s_list[0])):
    for j in range(len(s_list)):
        u = swipe_count(i, j, 0, -1) + 1
        ur = swipe_count(i, j, 1, -1) + 1
        r = swipe_count(i, j, 1, 0) + 1
        dr = swipe_count(i, j, 1, 1) + 1
        d = swipe_count(i, j, 0, 1) + 1
        dl = swipe_count(i, j, -1, 1) + 1
        l = swipe_count(i, j, -1, 0) + 1
        ul = swipe_count(i, j, -1, -1) + 1

        m = max([u, ur, r, dr, d, dl, l, ul])
        if max_count < m:
            max_count = m

print(max_count)
