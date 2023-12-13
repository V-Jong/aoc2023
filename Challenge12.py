import functools
import re
from collections import Counter
from itertools import combinations, product, permutations


def do_challenge():
    file = open('12/input.txt', 'r')
    lines = file.read().splitlines()

    sum_variants = 0
    # for comb in permutations(['#', '.', '#'], 3):
    #     print(f'Comb: {comb}')
    newlines = []
    for line in lines:
        line_split = line.split()
        grid = line_split[0]
        groups = line_split[1]
        new_grid = ''
        new_groups = ''
        for x in range(0, 5, 1):
            if x == 0:
                new_grid += grid
                new_groups += groups
            else:
                new_grid += '?' + grid
                new_groups += ',' + groups
        newlines.append(new_grid + ' ' + new_groups)

    for line in newlines:
        print(f'\nEvaluating line: {line}')
        line_split = line.split()
        grid = line_split[0]
        # print(f'Grid: {grid}')
        # print(f'Groups of springs: {line_split[1]}')
        groups = []
        for count in line_split[1].split(','):
            groups.append(int(count))

        # Filter out any groups that we can immediately match
        # for group in groups.copy():
        #     # print(f'Checking multiple {group}')
        #     index = grid.find(group)
        #     if index != -1:
        #         # print(f'Found {group} at index {index} of {grid}')
        #         # print(f'{index + len(group)} == {len(grid)}')
        #         # print(f'grid[index - 1] ({index - 1}) = {grid[index - 1]}')
        #         # print(f'line[index + len(group)] ({index + len(group)}) = {line[index + len(group)]}')
        #         if (index == 0 or grid[index - 1] == '.') and (index + len(group) == len(grid) or grid[index + len(group)] == '.'):
        #             grid = grid.replace(group, '', 1)
        #             # print(f'Updated line to {grid} and removing group {group}')
        #             groups.remove(group)
        #             # print(f'Groups after: {groups}')
        #
        # for match in re.findall('\.\?+#+\.*$', grid):
        #     match2 = match.replace('?', '#')
        #     match2 = match2.replace('.', '')
        #     print(f'Found matching 1 {match}')
        #     for g in [g for g in groups if g == match2]:
        #         grid = grid.replace(match.replace('.', ''), '', 1)
        #         groups.remove(g)
        #         print(f'Replaced match {match}, new grid: {grid}')
        # for match in re.findall('\.#+\?+\.*$', grid):
        #     print(f'Found matching 2 {match}')
        # for match in re.findall('^\.*\?+#+\.', grid):
        #     print(f'Found matching 3 {match}')
        # for match in re.findall('^\.*#+\?+\.', grid):
        #     print(f'Found matching 4 {match}')
        #
        # print(f'Replacing unnecessary dots in {grid}')
        # grid = re.sub('\.+', '.', grid)

        print(f'Remaining groups: {groups}')
        print(f'Remaining grid: {grid}')

        variants = calc(grid, tuple(groups))
        print(f'Number of variants for {grid} = {variants}')
        sum_variants += variants
    # test = get_combinations('????', '##.')
    # for t in test:
    #     if Counter(t)['#'] == 2:
    #         print(f'{t}')

    print(f'\nSum: {sum_variants}')


def solve(springs: str, groups: list[int], cache: dict, i: int, iteration: int):
    spaces = iteration * 10 * ' '
    print(f'\n{spaces}---- begin at index {i} for {springs} ----')
    print(f'{spaces}springs: {springs}')
    print(f'{spaces}groups: {groups}')

    if len(groups) == 0:
        for x in range(i, len(springs), 1):
            if springs[x] == '#':
                print(f'{spaces}# found in {springs} after index {x} -> no match, returning 0')
                return 0
        print(f'{spaces}no # found in {springs} after index {i} -> match, returning 1')
        return 1

    # advance i to the next available '?' or '#'
    for x in range(i, len(springs), 1):
        if springs[x] == '?' or springs[x] == '#':
            i = x
            print(f'{spaces}Set i to {i}')
            break

    if i > len(springs):
        print(f'{spaces}i > len(springs), returning 0')
        return 0

    if (i, len(groups)) in cache:
        print(f'{spaces}Match in cache for ({i}, {len(groups)}, returning {cache.get(i)})')
        return cache.get(i)

    result = 0
    next_group = groups[0]
    to_fill = springs[i:i + next_group]
    print(f'{spaces}Next group: {next_group}')
    print(f'{spaces}To fill (springs[{i}]): {to_fill}')
    if all(x == '?' or x == '#' for x in to_fill):
        new_i = i + next_group + 1
        groups.remove(next_group)
        print(f'{spaces}All can fit, moving to new iteration with i = {new_i} with groups {groups}')
        result += solve(springs, groups.copy(), cache, new_i, iteration + 1)

    if springs[i] == '?':
        new_i = i + 1
        print(f'{spaces}Char at index {i} of {springs} is ?, moving to new iteration with i = {new_i}')
        result += solve(springs, groups.copy(), cache, new_i, iteration + 1)

    cache.update({(i, len(groups)): result})
    print(f'{spaces}Returning result {result} for i = {i} in {springs}')
    return result


@functools.lru_cache(maxsize=None)
def calc(record, groups):

    # Did we run out of groups? We might still be valid
    if not groups:

        # Make sure there aren't any more damaged springs, if so, we're valid
        if "#" not in record:
            # This will return true even if record is empty, which is valid
            return 1
        else:
            # More damaged springs that we can't fit
            return 0

    # There are more groups, but no more record
    if not record:
        # We can't fit, exit
        return 0

    # Look at the next element in each record and group
    next_character = record[0]
    next_group = groups[0]

    # Logic that treats the first character as pound
    def pound():

        # If the first is a pound, then the first n characters must be
        # able to be treated as a pound, where n is the first group number
        this_group = record[:next_group]
        this_group = this_group.replace("?", "#")

        # If the next group can't fit all the damaged springs, then abort
        if this_group != next_group * "#":
            return 0

        # If the rest of the record is just the last group, then we're
        # done and there's only one possibility
        if len(record) == next_group:
            # Make sure this is the last group
            if len(groups) == 1:
                # We are valid
                return 1
            else:
                # There's more groups, we can't make it work
                return 0

        # Make sure the character that follows this group can be a seperator
        if record[next_group] in "?.":
            # It can be seperator, so skip it and reduce to the next group
            return calc(record[next_group+1:], groups[1:])

        # Can't be handled, there are no possibilites
        return 0

    # Logic that treats the first character as a dot
    def dot():
        # We just skip over the dot looking for the next pound
        return calc(record[1:], groups)

    if next_character == '#':
        # Test pound logic
        out = pound()

    elif next_character == '.':
        # Test dot logic
        out = dot()

    elif next_character == '?':
        # This character could be either character, so we'll explore both
        # possibilities
        out = dot() + pound()

    else:
        raise RuntimeError

    print(record, groups, out)
    return out
