N = int(input())
A_list = list()
B_list = list()
max_date = 0

for _ in range(N):
    A, B = [int(x) for x in input().split()]
    A_list.append(A)
    B_list.append(B)
    max_date = B if B > max_date else max_date

record = ['0'] * max_date

for i in range(N):
    A = A_list[i]
    B = B_list[i]
    record[A-1:B] = ['1'] * (B - A + 1)

record_parts = ''.join(record).split('0')

max_len_part = 0
for part in record_parts:
    if part == '':
        continue
    len_part = len(part)
    max_len_part = len_part if len_part > max_len_part else max_len_part

print(max_len_part)
