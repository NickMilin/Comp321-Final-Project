### This is only for creating an edge case to test the time_limit_exceeded solution

import os
import random

curr_dir = os.path.dirname(os.path.abspath(__file__))
data_secret_dir = os.path.join(curr_dir, '..', 'data', 'secret')

case = 3

if case == 1:
    file_name = os.path.join(data_secret_dir, 'secret1.in')
    N, M = 200000, 2000

    with open(file_name, 'w') as f:
        f.write(f'{N} {M}' + '\n')
        for i in range(M):
            f.write(f"1 {100*i+1} 1" + '\n')

        f.write("1" + '\n')
        f.write("100000")


if case == 2:
    file_name = os.path.join(data_secret_dir, 'secret2.in')
    N, M = 200000, 20
    Q = 2000

    with open(file_name, 'w') as f:
        f.write(f'{N} {M}' + '\n')
        for i in range(M):
            random_index_1 = random.randint(1, N)
            random_index_2 = random.randint(1, N)
            smallest_index = min(random_index_1, random_index_2)
            largest_index = max(random_index_1, random_index_2)

            value = random.randint(-100000,100000)

            f.write(f"{smallest_index} {largest_index} {value}" + '\n')

        f.write(f"{Q}" + '\n')
        for _ in range(Q):
            number_of_road_blocks = random.randint(1, 10)
            road_blocks = random.sample(range(1, N), number_of_road_blocks)
            road_blocks_string = ' '.join(map(str, road_blocks))
            f.write(road_blocks_string + '\n')


if case == 3:
    file_name = os.path.join(data_secret_dir, 'secret21.in')
    N, M = 2000000, 2500
    Q = 1

    with open(file_name, 'w') as f:
        f.write(f'{N} {M}' + '\n')
        for i in range(M):
            f.write(f"1 2000000 1000000" + '\n')

        f.write("1" + '\n')
        f.write("1000000")