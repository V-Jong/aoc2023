file = open('18/input.txt', 'r')
lines = file.read().splitlines()

grid = []
grid_spec = {}
total = []


def do_challenge():
    max_x = 0
    max_y = 0
    x = 0
    y = 0
    grid.append((x, y))
    for l_index, line in enumerate(lines):
        l_split = line.split()
        direction = l_split[0]
        move_count = int(l_split[1])
        for i in range(0, move_count, 1):
            if direction == 'R':
                x += 1
                if x > max_x:
                    max_x = x
            if direction == 'L':
                x -= 1
            if direction == 'U':
                y -= 1
            if direction == 'D':
                y += 1
                if y > max_y:
                    max_y = y
            # print(f'Adding to grid: {x, y}')
            if (x, y) not in grid:
                grid.append((x, y))
    print(f'Found {len(grid)} border items')
    print_debug('debug.txt', grid, max_x + 1, max_y + 1)
    print(f'Printed border items')

    grid_file = open('18/debug.txt', 'r')
    grid_lines = grid_file.read().splitlines()

    for l_index, grid_line in enumerate(grid_lines):
        grid_items = [*grid_line]
        for c_index, c in enumerate(grid_items):
            if c == '#':
                left_n = [(x, y) for (x, y) in grid if c_index - 1 == x and y == l_index]
                right_n = [(x, y) for (x, y) in grid if c_index + 1 == x and y == l_index]
                up_n = [(x, y) for (x, y) in grid if c_index == x and y == l_index - 1]
                down_n = [(x, y) for (x, y) in grid if c_index == x and y == l_index + 1]
                if len(left_n) == 1 and len(right_n) == 1:
                    corner = '-'
                if len(left_n) == 1 and len(down_n) == 1:
                    corner = '7'
                if len(left_n) == 1 and len(up_n) == 1:
                    corner = 'J'
                if len(right_n) == 1 and len(up_n) == 1:
                    corner = 'L'
                if len(right_n) == 1 and len(down_n) == 1:
                    corner = 'F'
                if len(up_n) == 1 and len(down_n) == 1:
                    corner = '|'
                grid_spec.update({(c_index, l_index): corner})
            if c == '.':
                grid_spec.update({(c_index, l_index): '.'})

    print_debug2('debug2.txt', grid_spec, max_x + 1, max_y + 1)

    grid2_file = open('18/debug2.txt', 'r')
    grid2_lines = grid2_file.read().splitlines()
    for l_index, grid_line in enumerate(grid2_lines):
        grid_items = [*grid_line]
        inside = False
        last_corner = ''
        for c_index, c in enumerate(grid_items):
            if c == '.':
                if inside:
                    print(f'dot at ({c_index}, {l_index}) is inside, adding')
                    total.append((c_index, l_index))
                    continue
            if c == '-':
                inside = not inside
                total.append((c_index, l_index))
                continue
            if c == '|':
                inside = not inside
                total.append((c_index, l_index))
                continue
            if ((last_corner == 'F' and c == '7') or (last_corner == '7' and c == 'F') or
                    (last_corner == 'J' and c == 'L') or (last_corner == 'L' and c == 'J')):
                inside = not inside
                total.append((c_index, l_index))
                continue
            if (last_corner == 'L' and c == '7') or (last_corner == '7' and c == 'L'):
                inside = True
                total.append((c_index, l_index))
                continue
            if c == 'F' or c == 'J' or c == '7' or c == 'L':
                total.append((c_index, l_index))
                last_corner = c
                inside = not inside
                continue
            print(f'char {c} at ({c_index}, {l_index}) not mapped')

    print(f'Found {len(total)} total items')


def print_debug(file_name: str, items: list, max_x: int, max_y: int):
    open('18/' + file_name, 'w').close()
    with open("18/" + file_name, "a") as f:
        for l_index in range(0, max_y, 1):
            n_line = ''
            for c_index in range(0, max_x, 1):
                if any(pn for pn in items if pn[0] == c_index and pn[1] == l_index):
                    n_line += '#'
                else:
                    n_line += '.'
            print(f'{n_line}', file=f)


def print_debug2(file_name: str, items: dict, max_x: int, max_y: int):
    open('18/' + file_name, 'w').close()
    with open("18/" + file_name, "a") as f:
        for l_index in range(0, max_y, 1):
            n_line = ''
            for c_index in range(0, max_x, 1):
                if any(pn for pn in items if pn[0] == c_index and pn[1] == l_index):
                    n_line += items.get((c_index, l_index))
                else:
                    n_line += '.'
            print(f'{n_line}', file=f)
