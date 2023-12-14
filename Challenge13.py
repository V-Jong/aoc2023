def do_challenge():
    file = open('13/test.txt', 'r')
    lines = file.read().splitlines()

    patterns = []
    pattern = []
    for line in lines:
        if len(line) == 0:
            patterns.append(pattern.copy())
            pattern = []
        else:
            pattern.append(line)
    patterns.append(pattern)

    print(f'Nr of patterns: {len(patterns)}')
    print(f'{patterns}')

    total = 0

    for pattern in patterns:
        print(f'Checking pattern: {pattern}')
        y_potentials = find_vertical_split(pattern, 0, [])
        x_potentials = find_horizontal_split(pattern, 0, [])
        # find_horizontal_split(pattern)
        potential_smudges = []

        print(f'Y split: {y_potentials}')
        print(f'X split: {x_potentials}')
        y_valid_list = []
        x_valid_list = []

        for y in y_potentials:
            y_valid = is_valid_vertical(pattern, y, y + 1, True, False, potential_smudges)
            print(f'{y} as y split is valid: {y_valid}')
            if y_valid:
                y_valid_list.append(y)
        for x in x_potentials:
            x_valid = is_valid_horizontal(pattern, x, x + 1, True, False, potential_smudges)
            print(f'{x} as x split is valid: {x_valid}')
            if x_valid:
                x_valid_list.append(x)

        print(f'Potential smudges: {potential_smudges}')
        final_pattern = pattern.copy()
        for potential_smudge in potential_smudges:
            line_to_edit = pattern[potential_smudge[0]]
            print(f'Testing smudge: {potential_smudge} on line: {line_to_edit}')
            char = line_to_edit[potential_smudge[1]]
            print(f'char to replace at index {potential_smudge[1]}: {char}')
            if char == '.':
                new_line = line_to_edit[:potential_smudge[1]] + '#' + line_to_edit[potential_smudge[1] + 1:]
            else:
                new_line = line_to_edit[:potential_smudge[1]] + '.' + line_to_edit[potential_smudge[1] + 1:]
            test_pattern = pattern.copy()
            test_pattern[potential_smudge[0]] = new_line
            with open("13/output.txt", "a") as f:
                for line in test_pattern:
                    print(f'{line}', file=f)
                print('', file=f)
            count_valid = calculate_valid(test_pattern, y_valid_list, x_valid_list)
            if count_valid == 1:
                final_pattern = test_pattern
                break

        print(f'After fixing, final pattern: {final_pattern}')
        y_potentials = find_vertical_split(final_pattern, 0, [])
        x_potentials = find_horizontal_split(final_pattern, 0, [])

        print(f'Y split final: {y_potentials}')
        print(f'X split final: {x_potentials}')

        for y in y_potentials:
            y_valid = is_valid_vertical(final_pattern, y, y + 1, True, False, [])
            if y_valid and y not in y_valid_list:
                print(f'{y} as y split is valid: {y_valid}')
                total += y + 1
        for x in x_potentials:
            x_valid = is_valid_horizontal(final_pattern, x, x + 1, True, False, [])
            if x_valid and x not in x_valid_list:
                print(f'{x} as x split is valid: {x_valid}')
                total += (x + 1) * 100

        print()

    print(f'\nSum: {total}')


def find_horizontal_split(pattern: list[str], top_row_index: int, matches: list[int]):
    bottom_row_index = top_row_index + 1
    limit = len(pattern) - 1
    if bottom_row_index > limit:
        return matches

    top_row = []
    bottom_row = []
    rows_matching = True

    top_line = pattern[top_row_index]
    bottom_line = pattern[bottom_row_index]

    for c_index, char in enumerate(top_line):
        top_row.append(char)
        bottom_row.append(bottom_line[c_index])

    for t_index, t_char in enumerate(top_row):
        if t_char != bottom_row[t_index]:
            rows_matching = False
            break
    # If matching then proceed to check next couple
    if rows_matching:
        # print(f'Lines ({top_row_index}, {bottom_row_index}) matching, returning top')
        matches.append(top_row_index)
    return find_horizontal_split(pattern, top_row_index + 1, matches)


def find_vertical_split(pattern: list[str], left_col_index: int, matches: list[int]):
    right_col_index = left_col_index + 1
    limit = len(pattern[0]) - 1
    if right_col_index > limit:
        return matches

    left_col = []
    right_col = []
    cols_matching = True

    for line in pattern:
        left_col.append(line[left_col_index])
        right_col.append(line[right_col_index])

    for l_index, l_char in enumerate(left_col):
        if l_char != right_col[l_index]:
            cols_matching = False
            break
    # If matching then proceed to check next couple
    if cols_matching:
        # print(f'Lines ({left_col_index}, {right_col_index}) matching, returning left')
        matches.append(left_col_index)
    return find_vertical_split(pattern, left_col_index + 1, matches)


def is_valid_vertical(pattern: list[str], last_valid_left: int, last_valid_right: int, current_valid: bool, fix: bool, smudges: []):
    l_to_check = last_valid_left - 1
    r_to_check = last_valid_right + 1
    if l_to_check < 0 or r_to_check >= len(pattern[0]):
        return True

    left_col = []
    right_col = []

    for line in pattern:
        left_col.append(line[l_to_check])
        right_col.append(line[r_to_check])

    for l_index, l_char in enumerate(left_col):
        if l_char != right_col[l_index]:
            if fix:
                line_to_edit = pattern[l_index]
                new_line = line_to_edit[:l_to_check] + right_col[l_index] + line_to_edit[l_to_check + 1:]
                print(f'replacing vertical at index {l_index} {line_to_edit} with {new_line}')
                pattern[l_index] = new_line
                return current_valid and is_valid_vertical(pattern, last_valid_left, last_valid_right, current_valid, fix, smudges)
            else:
                smudges.append((l_index, r_to_check))
                smudges.append((l_index, r_to_check))
                return False

    return current_valid and is_valid_vertical(pattern, l_to_check, r_to_check, current_valid, fix, smudges)


def is_valid_horizontal(pattern: list[str], last_valid_top: int, last_valid_bottom: int, current_valid: bool, fix: bool, smudges: []):
    t_to_check = last_valid_top - 1
    b_to_check = last_valid_bottom + 1
    if t_to_check < 0 or b_to_check >= len(pattern):
        return True

    top_row = []
    bottom_row = []

    top_line = pattern[t_to_check]
    bottom_line = pattern[b_to_check]

    for c_index, char in enumerate(top_line):
        top_row.append(char)
        bottom_row.append(bottom_line[c_index])

    for t_index, t_char in enumerate(top_row):
        if t_char != bottom_row[t_index]:
            if fix:
                print(f'replacing horizontal at index {t_to_check} {pattern[t_to_check]} with {bottom_line}')
                pattern[t_to_check] = bottom_line
                return current_valid and is_valid_horizontal(pattern, last_valid_top, last_valid_bottom, current_valid, fix, smudges)
            else:
                smudges.append((t_to_check, t_index))
                smudges.append((b_to_check, t_index))
                return False

    return current_valid and is_valid_horizontal(pattern, t_to_check, b_to_check, current_valid, fix, smudges)


def calculate_valid(pattern: list[str], y_to_skip: list[int], x_to_skip: list[int]):
    print(f'Calculating valid')
    count_valid = 0
    y_potentials = find_vertical_split(pattern, 0, [])
    x_potentials = find_horizontal_split(pattern, 0, [])
    print(f'y potentials: {y_potentials}')
    print(f'x potentials: {x_potentials}')

    for y in y_potentials:
        y_valid = is_valid_vertical(pattern, y, y + 1, True, False, [])
        # print(f'{y} as y split is valid: {y_valid}')
        if y_valid and y not in y_to_skip:
            count_valid += 1
    for x in x_potentials:
        x_valid = is_valid_horizontal(pattern, x, x + 1, True, False, [])
        # print(f'{x} as x split is valid: {x_valid}')
        if x_valid and x not in x_to_skip:
            count_valid += 1
    print(f'Calculating valid return {count_valid}')
    return count_valid
