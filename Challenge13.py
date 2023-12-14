def do_challenge():
    file = open('13/input.txt', 'r')
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

        print(f'Y split: {y_potentials}')
        print(f'X split: {x_potentials}')

        for y in y_potentials:
            y_valid = is_valid_vertical(pattern, y, y + 1, True)
            print(f'{y} as y split is valid: {y_valid}')
            if y_valid:
                total += y + 1
        for x in x_potentials:
            x_valid = is_valid_horizontal(pattern, x, x + 1, True)
            print(f'{x} as x split is valid: {x_valid}')
            if x_valid:
                total += (x + 1) * 100

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


def is_valid_vertical(pattern: list[str], last_valid_left: int, last_valid_right: int, current_valid: bool):
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
            return False

    return current_valid and is_valid_vertical(pattern, l_to_check, r_to_check, current_valid)


def is_valid_horizontal(pattern: list[str], last_valid_top: int, last_valid_bottom: int, current_valid: bool):
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
            return False

    return current_valid and is_valid_horizontal(pattern, t_to_check, b_to_check, current_valid)
