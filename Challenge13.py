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

    for pattern in patterns:
        print(f'Checking pattern: {pattern}')
        y_potentials = find_vertical_split(pattern, 0, [])
        x_potentials = find_horizontal_split(pattern, 0, [])
        # find_horizontal_split(pattern)

        print(f'Y split: {y_potentials}')
        print(f'X split: {x_potentials}')


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
        print(f'Lines ({top_row_index}, {bottom_row_index}) matching, returning top')
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
        print(f'Lines ({left_col_index}, {right_col_index}) matching, returning left')
        matches.append(left_col_index)
    return find_vertical_split(pattern, left_col_index + 1, matches)


