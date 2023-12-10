from itertools import product, groupby


class Node:
    def __init__(self, key, x, y):
        self.key = key
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.key} - ({self.x}, {self.y})'

    def __repr__(self):
        return f'{self.key} - ({self.x}, {self.y})'


def do_challenge():
    do_challenge_a()


def do_challenge_a():
    file = open('10/input.txt', 'r')
    lines = file.readlines()

    max_y = len(lines)
    max_x = 0
    nodes = []
    for line_index, line in enumerate(lines):
        line = line.replace('\n', '')
        line_split = [*line]
        max_x = len(line_split)
        for c_index, c in enumerate(line_split):
            nodes.append(Node(c, c_index + 1, line_index + 1))

    start_node = [item for item in nodes if item.key == 'S'][0]
    ignore_list = []
    steps = 0
    current_node = start_node
    start_found = False
    with open("10/output.txt", "a") as f:
        while not start_found:
            # print(f'\nChecking node {current_node}', file=f)
            if current_node.key == start_node.key and steps > 1:
                start_found = True
                break
            copy_current = Node(current_node.key, current_node.x, current_node.y)
            if current_node.key != 'S' and not any(ignored for ignored in ignore_list if current_node.x == ignored.x and current_node.y == ignored.y):
                ignore_list.append(current_node)
            if current_node.key == 'S':
                left_node = [item for item in nodes if item.x == current_node.x - 1 and item.y == current_node.y and
                             (item.key == '-' or item.key == 'L' or item.key == 'F') and
                             not any(ignored for ignored in ignore_list if item.x == ignored.x and item.y == ignored.y)]
                if (len(left_node)) > 0:
                    print(f'Potential lefts {left_node}', file=f)
                    ignore_list.append(left_node[0])
                    steps += 1
                    current_node = left_node[0]
                    continue
                right_node = [item for item in nodes if item.x == current_node.x + 1 and item.y == current_node.y and
                              (item.key == '-' or item.key == 'J' or item.key == '7') and
                              not any(ignored for ignored in ignore_list if item.x == ignored.x and item.y == ignored.y)]
                if (len(right_node)) > 0:
                    print(f'Potential rights {right_node}', file=f)
                    ignore_list.append(right_node[0])
                    steps += 1
                    current_node = right_node[0]
                    continue
                top_node = [item for item in nodes if item.x == current_node.x and item.y == current_node.y - 1 and
                            (item.key == '|' or item.key == '7' or item.key == 'F') and
                            not any(ignored for ignored in ignore_list if item.x == ignored.x and item.y == ignored.y)]
                if (len(top_node)) > 0:
                    print(f'Potential tops {top_node}', file=f)
                    ignore_list.append(top_node[0])
                    steps += 1
                    current_node = top_node[0]
                    continue
                bottom_node = [item for item in nodes if item.x == current_node.x and item.y == current_node.y + 1 and
                               (item.key == '|' or item.key == 'J' or item.key == 'L') and
                               not any(ignored for ignored in ignore_list if item.x == ignored.x and item.y == ignored.y)]
                if (len(bottom_node)) > 0:
                    print(f'Potential bottoms {bottom_node}', file=f)
                    ignore_list.append(bottom_node[0])
                    steps += 1
                    current_node = bottom_node[0]
                    continue
            if current_node.key == '-':
                left_node = [item for item in nodes if item.x == current_node.x - 1 and item.y == current_node.y and
                             (item.key == '-' or item.key == 'L' or item.key == 'F' or (item.key == 'S' and steps > 2)) and
                             not any(ignored for ignored in ignore_list if item.x == ignored.x and item.y == ignored.y)]
                if (len(left_node)) > 0:
                    print(f'Potential lefts {left_node}', file=f)
                    ignore_list.append(left_node[0])
                    steps += 1
                    current_node = left_node[0]
                    continue
                right_node = [item for item in nodes if item.x == current_node.x + 1 and item.y == current_node.y and
                              (item.key == '-' or item.key == 'J' or item.key == '7' or (item.key == 'S' and steps > 2)) and
                              not any(ignored for ignored in ignore_list if item.x == ignored.x and item.y == ignored.y)]
                if (len(right_node)) > 0:
                    print(f'Potential rights {right_node}', file=f)
                    ignore_list.append(right_node[0])
                    steps += 1
                    current_node = right_node[0]
                    continue
            if current_node.key == '|':
                top_node = [item for item in nodes if item.x == current_node.x and item.y == current_node.y - 1 and
                            (item.key == '|' or item.key == '7' or item.key == 'F' or (item.key == 'S' and steps > 2)) and
                            not any(ignored for ignored in ignore_list if item.x == ignored.x and item.y == ignored.y)]
                if (len(top_node)) > 0:
                    print(f'Potential tops {top_node}', file=f)
                    ignore_list.append(top_node[0])
                    steps += 1
                    current_node = top_node[0]
                    continue
                bottom_node = [item for item in nodes if item.x == current_node.x and item.y == current_node.y + 1 and
                               (item.key == '|' or item.key == 'J' or item.key == 'L' or (item.key == 'S' and steps > 2)) and
                               not any(ignored for ignored in ignore_list if item.x == ignored.x and item.y == ignored.y)]
                if (len(bottom_node)) > 0:
                    print(f'Potential bottoms {bottom_node}', file=f)
                    ignore_list.append(bottom_node[0])
                    steps += 1
                    current_node = bottom_node[0]
                    continue
            if current_node.key == 'F':
                right_node = [item for item in nodes if item.x == current_node.x + 1 and item.y == current_node.y and
                              (item.key == '-' or item.key == 'J' or item.key == '7' or (item.key == 'S' and steps > 2)) and
                              not any(ignored for ignored in ignore_list if item.x == ignored.x and item.y == ignored.y)]
                if (len(right_node)) > 0:
                    print(f'Potential rights {right_node}', file=f)
                    ignore_list.append(right_node[0])
                    steps += 1
                    current_node = right_node[0]
                    continue
                bottom_node = [item for item in nodes if item.x == current_node.x and item.y == current_node.y + 1 and
                               (item.key == '|' or item.key == 'J' or item.key == 'L' or (item.key == 'S' and steps > 2)) and
                               not any(ignored for ignored in ignore_list if item.x == ignored.x and item.y == ignored.y)]
                if (len(bottom_node)) > 0:
                    print(f'Potential bottoms {bottom_node}', file=f)
                    ignore_list.append(bottom_node[0])
                    steps += 1
                    current_node = bottom_node[0]
                    continue
            if current_node.key == '7':
                left_node = [item for item in nodes if item.x == current_node.x - 1 and item.y == current_node.y and
                             (item.key == '-' or item.key == 'L' or item.key == 'F' or (item.key == 'S' and steps > 2)) and
                             not any(ignored for ignored in ignore_list if item.x == ignored.x and item.y == ignored.y)]
                if (len(left_node)) > 0:
                    print(f'Potential lefts {left_node}', file=f)
                    ignore_list.append(left_node[0])
                    steps += 1
                    current_node = left_node[0]
                    continue
                bottom_node = [item for item in nodes if item.x == current_node.x and item.y == current_node.y + 1 and
                               (item.key == '|' or item.key == 'J' or item.key == 'L' or (item.key == 'S' and steps > 2)) and
                               not any(ignored for ignored in ignore_list if item.x == ignored.x and item.y == ignored.y)]
                if (len(bottom_node)) > 0:
                    print(f'Potential bottoms {bottom_node}', file=f)
                    ignore_list.append(bottom_node[0])
                    steps += 1
                    current_node = bottom_node[0]
                    continue
            if current_node.key == 'L':
                right_node = [item for item in nodes if item.x == current_node.x + 1 and item.y == current_node.y and
                              (item.key == '-' or item.key == 'J' or item.key == '7' or (item.key == 'S' and steps > 2)) and
                              not any(ignored for ignored in ignore_list if item.x == ignored.x and item.y == ignored.y)]
                if (len(right_node)) > 0:
                    print(f'Potential rights {right_node}', file=f)
                    ignore_list.append(right_node[0])
                    steps += 1
                    current_node = right_node[0]
                    continue
                top_node = [item for item in nodes if item.x == current_node.x and item.y == current_node.y - 1 and
                            (item.key == '|' or item.key == '7' or item.key == 'F' or (item.key == 'S' and steps > 2)) and
                            not any(ignored for ignored in ignore_list if item.x == ignored.x and item.y == ignored.y)]
                if (len(top_node)) > 0:
                    print(f'Potential tops {top_node}', file=f)
                    ignore_list.append(top_node[0])
                    steps += 1
                    current_node = top_node[0]
                    continue
            if current_node.key == 'J':
                left_node = [item for item in nodes if item.x == current_node.x - 1 and item.y == current_node.y and
                             (item.key == '-' or item.key == 'L' or item.key == 'F' or (item.key == 'S' and steps > 2)) and
                             not any(ignored for ignored in ignore_list if item.x == ignored.x and item.y == ignored.y)]
                if (len(left_node)) > 0:
                    print(f'Potential lefts {left_node}', file=f)
                    ignore_list.append(left_node[0])
                    steps += 1
                    current_node = left_node[0]
                    continue
                top_node = [item for item in nodes if item.x == current_node.x and item.y == current_node.y - 1 and
                            (item.key == '|' or item.key == '7' or item.key == 'F' or (item.key == 'S' and steps > 2)) and
                            not any(ignored for ignored in ignore_list if item.x == ignored.x and item.y == ignored.y)]
                if (len(top_node)) > 0:
                    print(f'Potential tops {top_node}', file=f)
                    ignore_list.append(top_node[0])
                    steps += 1
                    current_node = top_node[0]
                    continue
                if current_node.x == copy_current.x and current_node.y == copy_current.y:
                    current_node = ignore_list[-1]
                    ignore_list.remove(current_node)
                    ignore_list.append(copy_current)
                    print(f'Found nowhere to move from {current_node}, going back to previous node')
                    continue

    with open("10/input3.txt", "a") as f3:
        for l_index, line in enumerate(lines):
            l_split = [*line.strip()]
            for c_index, c in enumerate(l_split.copy()):
                match_in_loop = [m for m in ignore_list if m.x - 1 == c_index and m.y - 1 == l_index]
                if len(match_in_loop) > 0:
                    l_split[c_index] = '@'
            print(f'{"".join(l_split)}', file=f3)


    # print(f'Ignore list {ignore_list}')
    print(f'Steps back to S: {steps}')
    # print(f'Steps to farthest: {int(steps / 2)}')

    rogue_tiles = [rogue for rogue in nodes if not any(r for r in ignore_list if r.x == rogue.x and r.y == rogue.y)]
    print(f'Max x: {max_x}, max y: {max_y}')
    # print(f'Rogue tiles: {rogue_tiles}')
    rogue_tiles2 = list(map(lambda t: (t.x, t.y), rogue_tiles))
    # print(f'Coordinates: {rogue_tiles2}')

    man_tups = [sorted(sub) for sub in product(rogue_tiles2, repeat=2) if manhattan(*sub) == 1]

    res_dict = {ele: {ele} for ele in rogue_tiles2}
    for tup1, tup2 in man_tups:
        res_dict[tup1] |= res_dict[tup2]
        res_dict[tup2] = res_dict[tup1]

    groups = [[*next(val)] for key, val in groupby(sorted(res_dict.values(), key=id), id)]
    groups_dict = {}

    print()
    for group in groups:
        # print(f'group: {group}')
        groups_dict.update({group[0]: group})

    print()
    encloseds = []
    for value in groups_dict.values():
        print(f'Vals: {value}')
        if not any((x, y) for (x, y) in value if x == 1 or y == 1 or x == max_x or y == max_y):
            encloseds.append(value)

    for enclosed in encloseds:
        print(f'Enclosed: {enclosed}')

    print()
    count_enclosed = 0
    with open("10/output2.txt", "a") as f2:
        for enclosed in encloseds:
            print(f'\nEnclosed: {enclosed}', file=f2)
            in_wall = False
            line = lines[enclosed[0][1] - 1]
            print(f'checking char position {enclosed[0]} in line {line.strip()}', file=f2)
            last_turn = -1
            for i in range(0, enclosed[0][0], 1):
                print(f'char at {i}: {line[i]}', file=f2)
                if line[i] == '.' or line[i] == 'O' or line[i] == 'I':
                    continue
                if line[i] == '-':
                    continue
                if line[i] == '|':
                    if any(wall for wall in nodes if wall.x == i):
                        in_wall = not in_wall
                        print(f'Switched in wall to {in_wall} due to |', file=f2)
                        continue
                if ((last_turn == 'J' and line[i] == 'L') or (last_turn == 'L' and line[i] == 'J') or
                        (last_turn == '7' and line[i] == 'F') or (last_turn == 'F' and line[i] == '7')):
                    in_wall = not in_wall
                    print(f'Switched in wall to {in_wall} due to combination {last_turn}{line[i]}', file=f2)
                    last_turn = line[i]
                    continue
                if line[i] == 'J' or line[i] == '7' or line[i] == 'L' or line[i] == 'F':
                    last_turn = line[i]
                    if line[i] == 'L' or line[i] == 'F':
                        in_wall = not in_wall
                        print(f'Set last char to {last_turn} and switched in wall to {in_wall}', file=f2)
                    else:
                        print(f'Set last char to {last_turn} and in wall remained {in_wall}', file=f2)
                    continue
            print(f'in_wall status: {in_wall}', file=f2)
            if in_wall:
                print(f'char {enclosed} inside wall', file=f2)
                count_enclosed += len(enclosed)

    print()
    print(f'Count enclosed: {count_enclosed}')


def manhattan(tup1, tup2):
    return abs(tup1[0] - tup2[0]) + abs(tup1[1] - tup2[1])
