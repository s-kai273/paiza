N, H, W, P, Q = [int(x) for x in input().strip().split()]

reserved_seat_list = [['available'] * W for _ in range(H)]

for i in range(N):
    p, q = input().split()
    reserved_seat_list[int(p)][int(q)] = 'reserved'

is_found = False
target_len = 0

while not is_found:
    for d in range(target_len + 1):
        p_delta = d
        q_delta = target_len - d

        point_list = set([
            (P + p_delta, Q + q_delta),
            (P + p_delta, Q - q_delta),
            (P - p_delta, Q + q_delta),
            (P - p_delta, Q - q_delta),
        ])

        for (p, q) in point_list:
            if p >= 0 and p < H and \
               q >= 0 and q < W and \
               reserved_seat_list[p][q] == 'available':
                print('{} {}'.format(p, q))
                is_found = True

    if is_found:
        break
    target_len += 1
