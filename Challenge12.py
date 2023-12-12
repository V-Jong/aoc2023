import re
from collections import Counter
from itertools import combinations, product


def do_challenge():
    file = open('12/test.txt', 'r')
    lines = file.read().splitlines()

    sum_variants = 0
    # for comb in combinations([1, 1, 2], 3):
    #     print(f'Comb: {comb}')
    for line in lines:
        print(f'\nEvaluating line: {line}')
        line_split = line.split()
        grid = line_split[0]
        # print(f'Grid: {grid}')
        # print(f'Groups of springs: {line_split[1]}')
        groups = []
        for count in line_split[1].split(','):
            groups.append(int(count) * '#')

        # Filter out any groups that we can immediately match
        for group in groups.copy():
            # print(f'Checking multiple {group}')
            index = grid.find(group)
            if index != -1:
                # print(f'Found {group} at index {index} of {grid}')
                # print(f'{index + len(group)} == {len(grid)}')
                # print(f'grid[index - 1] ({index - 1}) = {grid[index - 1]}')
                # print(f'line[index + len(group)] ({index + len(group)}) = {line[index + len(group)]}')
                if (index == 0 or grid[index - 1] == '.') and (index + len(group) == len(grid) or grid[index + len(group)] == '.'):
                    grid = grid.replace(group, '', 1)
                    # print(f'Updated line to {grid} and removing group {group}')
                    groups.remove(group)
                    # print(f'Groups after: {groups}')

        for match in re.findall('\.\?+#+\.*$', grid):
            match2 = match.replace('?', '#')
            match2 = match2.replace('.', '')
            print(f'Found matching 1 {match}')
            if any(g for g in groups if g == match2):
                grid = grid.replace(match.replace('.', ''), '', 1)
                print(f'Replaced match {match}, new grid: {grid}')
        for match in re.findall('\.#+\?+\.*$', grid):
            print(f'Found matching 2 {match}')
        for match in re.findall('^\.*\?+#+\.', grid):
            print(f'Found matching 3 {match}')
        for match in re.findall('^\.*#+\?+\.', grid):
            print(f'Found matching 4 {match}')

        print(f'Replacing unnecessary dots in {grid}')
        grid = re.sub('\.+', '.', grid)

        print(f'Remaining groups: {groups}')
        print(f'Remaining grid: {grid}')

        variants = 0
        sum_variants += variants
    # test = get_combinations('????', '##.')
    # for t in test:
    #     if Counter(t)['#'] == 2:
    #         print(f'{t}')

    print(f'Sum: {sum_variants}')


def get_combinations(text: str, char_to_fit: str):
    combs = []
    for sub in product((True, False), repeat=len(text)):
        combs.append("".join(char if ele else char_to_fit for char, ele in zip(text, sub)))
    return combs

