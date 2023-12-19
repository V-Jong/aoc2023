import re

file_pre = open('18/test.txt', 'r')
lines_pre = file_pre.read().splitlines()

grid = []
fixed_grid = []
grid_spec = {}
total = []


def do_challenge():
    open('18/input_fixed.txt', 'w').close()
    with open("18/input_fixed.txt", "a") as f:
        for lines in lines_pre:
            l_split = lines.split()
            hexa = re.findall('\w+', l_split[2])[0]
            direction_nr = int(hexa[-1])
            hex_a = hexa[:-1]
            # print(f'Processing hex: {hex_a} and direction: {direction_nr}')
            hex_val = int(hex_a, 16)
            if direction_nr == 0:
                direction = 'R'
            if direction_nr == 1:
                direction = 'D'
            if direction_nr == 2:
                direction = 'L'
            if direction_nr == 3:
                direction = 'U'
            print(f'{direction} {hex_val}', file=f)

    do_challenge_a()


def do_challenge_a():
    max_x = 0
    max_y = 0
    x = 0
    y = 0
    grid.append((x, y))
    file = open('18/input_fixed.txt', 'r')
    lines = file.read().splitlines()
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

    # Fix negative positions
    min_x = min(grid, key=lambda g: g[0])[0]
    min_y = min(grid, key=lambda g: g[1])[1]
    print(f'Max x = {max_x}, max y = {max_y}')
    max_x = max_x - min_x
    max_y = max_y - min_y
    print(f'New max x = {max_x}, new max y = {max_y}')
    print(f'Min x = {min_x}, min y = {min_y}')
    for (x, y) in grid:
        x = x - min_x
        y = y - min_y
        fixed_grid.append((x, y))

    print_debug('debug.txt', fixed_grid, max_x + 1, max_y + 1)
    print(f'Printed border items')

    grid_file = open('18/debug.txt', 'r')
    grid_lines = grid_file.read().splitlines()

    for l_index, grid_line in enumerate(grid_lines):
        grid_items = [*grid_line]
        for c_index, c in enumerate(grid_items):
            if c == '#':
                left_n = [(x, y) for (x, y) in fixed_grid if c_index - 1 == x and y == l_index]
                right_n = [(x, y) for (x, y) in fixed_grid if c_index + 1 == x and y == l_index]
                up_n = [(x, y) for (x, y) in fixed_grid if c_index == x and y == l_index - 1]
                down_n = [(x, y) for (x, y) in fixed_grid if c_index == x and y == l_index + 1]
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
                    # print(f'dot at ({c_index}, {l_index}) is inside, adding')
                    total.append((c_index, l_index))
                    continue
            if c == '-':
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
                print(f'Combination found {last_corner} and {c}, setting inside to {inside}')
                last_corner = c
                continue
            if c == 'F' or c == 'J' or c == '7' or c == 'L':
                total.append((c_index, l_index))
                # last_corner = c
                inside = not inside
                print(f'Found corner {c} at ({c_index}, {l_index}), switching inside to {inside}')

                if ((last_corner == 'L' and c == '7') or
                        (last_corner == 'F' and c == 'J')):
                    inside = not inside
                    # total.append((c_index, l_index))
                    print(f'Combination found {last_corner} and {c}, setting inside to {inside}')
                    last_corner = c
                    continue
                last_corner = c
                continue
            print(f'char {c} at ({c_index}, {l_index}) not mapped')
    print_debug('debug3.txt', total, max_x + 1, max_y + 1)

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
