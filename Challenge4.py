def do_challenge():
    do_challenge_b()


def do_challenge_a():
    file = open('4/test.txt', 'r')
    lines = file.readlines()

    total_points = 0
    with open("4/output.txt", "a") as f:
        for line_index, line in enumerate(lines):
            line = line.replace('\n', '')
            card_info = line.split(':')
            numbers = card_info[1].split('|')
            winning_numbers = [int(i) for i in numbers[0].strip().split()]
            pulled_numbers = [int(i) for i in numbers[1].strip().split()]
            common_numbers = intersection(winning_numbers, pulled_numbers)

            points = 0
            count_common = len(common_numbers)
            print(f'Common numbers: {common_numbers} ({count_common})')
            if count_common > 0:
                points = 2 ** (count_common - 1)
            print(f'Line has winning {winning_numbers} and pulled {pulled_numbers}, points: {points}\n')
            total_points += points

        print(f'Total points: {total_points}')


def do_challenge_b():
    file = open('4/test.txt', 'r')
    lines = file.readlines()

    total_points = 0
    with open("4/output.txt", "a") as f:
        for line_index, line in enumerate(lines):
            line = line.replace('\n', '')
            card_info = line.split(':')
            numbers = card_info[1].split('|')
            winning_numbers = [int(i) for i in numbers[0].strip().split()]
            pulled_numbers = [int(i) for i in numbers[1].strip().split()]
            common_numbers = intersection(winning_numbers, pulled_numbers)

            points = 0
            count_common = len(common_numbers)
            print(f'Common numbers: {common_numbers} ({count_common})')
            if count_common > 0:
                points = 2 ** (count_common - 1)
            print(f'Line has winning {winning_numbers} and pulled {pulled_numbers}, points: {points}\n')
            total_points += points

        print(f'Total points: {total_points}')


def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3
