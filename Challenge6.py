import re
from math import ceil, floor


def do_challenge():
    file = open('6/input.txt', 'r')
    lines = file.readlines()

    # times = re.findall(r'\d+', lines[0].split(':')[1].replace('\n', ''))
    times = [lines[0].split(':')[1].replace('\n', '').replace(' ', '')]
    print(f'Times {times}')
    # records = re.findall(r'\d+', lines[1].split(':')[1].replace('\n', ''))
    records = [lines[1].split(':')[1].replace('\n', '').replace(' ', '')]
    print(f'Records {records}')
    wins = 1
    with open("6/output.txt", "a") as f:
        for time_index, time in enumerate(times):
            time = int(time)
            record = int(records[time_index])
            count_win = solve(time, record)
            # for i in range(0, time, 1):
            #     speed = time - i
            #     rest_time = time - speed
            #     c_record = speed * rest_time
            #     # print(f'Checking {i}, speed {speed}, rest time {rest_time}, record {record}, current {c_record}')
            #     if c_record > record:
            #         count_win += 1
            if count_win > 0:
                wins = wins * count_win

        print(f'Wins: {wins}')


def solve(t, d):
    delta = (t**2 - 4*d)**0.5
    lo, hi = (t - delta) / 2, (t + delta) / 2
    return ceil(hi) - floor(lo) - 1
