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
    file = open('10/input.txt', 'r')
    lines = file.readlines()

    nodes = []
    for line_index, line in enumerate(lines):
        line = line.replace('\n', '')
        line_split = [*line]
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

    print(f'Steps: {int(steps / 2)}')
