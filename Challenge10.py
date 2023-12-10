import sys


class Node:
    def __init__(self, key, x, y):
        self.key = key
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self.key} | x: {self.x} | y: {self.y}'

    def __repr__(self):
        return f'{self.key} | x: {self.x} | y: {self.y}'


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
    ignore_list = [start_node]
    search = [item for item in nodes if item.x == 20 and item.y == 113]
    print(f'Search: {search}')
    # print(f'Nodes: {nodes}. \nStart: {start_node}')
    steps = int(count_steps_to_start(start_node, nodes, 1, start_node, True, ignore_list) / 2)
    print(f'Steps: {steps}')


def count_steps_to_start(current_node: Node, nodes: list[Node], steps: int, start_node: Node, ignore_start: bool, to_ignore: list[Node]):
    print(f'Checking node {current_node}')
    if current_node.key == start_node.key and not ignore_start:
        print(f'Found start again!')
        return 0
    if current_node.key == 'S':
        left_node = [item for item in nodes if item.x == current_node.x - 1 and item.y == current_node.y]
        if (len(left_node)) > 0 and (left_node[0].key == '-' or left_node[0].key == 'L' or left_node[0].key == 'F'):
            known_left = [item for item in to_ignore if item.x == left_node[0].x and item.y == left_node[0].y]
            if len(known_left) == 0 or known_left[0].key == start_node.key:
                print(f'Left found {left_node[0]}')
                to_ignore.append(left_node[0])
                steps += 1
                return count_steps_to_start(left_node[0], nodes, steps, start_node, False, to_ignore)
            else:
                print(f'Left is already known and is not start')
        else:
            print(f'No left node, stopping')
        right_node = [item for item in nodes if item.x == current_node.x + 1 and item.y == current_node.y and (item.key == '-' or item.key == 'J' or item.key == '7')]
        if (len(right_node)) > 0:
            print(f'Potential rights {right_node}')
            known_right = [item for item in to_ignore if item.x == right_node[0].x and item.y == right_node[0].y]
            if len(known_right) == 0 or right_node[0].key == start_node.key:
                print(f'Right found {right_node[0]}')
                to_ignore.append(right_node[0])
                steps += 1
                return count_steps_to_start(right_node[0], nodes, steps, start_node, False, to_ignore)
            else:
                print(f'Right is already known and is not start')
        else:
            print(f'No right node, stopping')
        top_node = [item for item in nodes if item.x == current_node.x and item.y == current_node.y - 1]
        if (len(top_node)) > 0 and (top_node[0].key == '|' or top_node[0].key == '7' or top_node[0].key == 'F'):
            known_top = [item for item in to_ignore if item.x == top_node[0].x and item.y == top_node[0].y]
            if len(known_top) == 0 or top_node[0].key == start_node.key:
                print(f'Top found {top_node[0]}')
                to_ignore.append(top_node[0])
                steps += 1
                return count_steps_to_start(top_node[0], nodes, steps, start_node, False, to_ignore)
            else:
                print(f'Top is already known and is not start')
        else:
            print(f'No top node, stopping')
        bottom_node = [item for item in nodes if item.x == current_node.x and item.y == current_node.y + 1]
        if (len(bottom_node)) > 0 and (bottom_node[0].key == '|' or bottom_node[0].key == 'J' or bottom_node[0].key == 'L'):
            known_bottom = [item for item in to_ignore if item.x == bottom_node[0].x and item.y == bottom_node[0].y]
            if len(known_bottom) == 0 or bottom_node[0].key == start_node.key:
                print(f'Bottom found {bottom_node[0]}')
                to_ignore.append(bottom_node[0])
                steps += 1
                return count_steps_to_start(bottom_node[0], nodes, steps, start_node, False, to_ignore)
            else:
                print(f'Bottom is already known and is not start')
        else:
            print(f'No bottom node, stopping')
    if current_node.key == '-':
        left_node = [item for item in nodes if item.x == current_node.x - 1 and item.y == current_node.y]
        if (len(left_node)) > 0 and (left_node[0].key == '-' or left_node[0].key == 'L' or left_node[0].key == 'F'):
            known_left = [item for item in to_ignore if item.x == left_node[0].x and item.y == left_node[0].y]
            if len(known_left) == 0 or known_left[0].key == start_node.key:
                print(f'Left found {left_node[0]}')
                to_ignore.append(left_node[0])
                steps += 1
                return count_steps_to_start(left_node[0], nodes, steps, start_node, False, to_ignore)
            else:
                print(f'Left is already known and is not start')
        else:
            print(f'No left node, stopping')
        right_node = [item for item in nodes if item.x == current_node.x + 1 and item.y == current_node.y and (
                    item.key == '-' or item.key == 'J' or item.key == '7')]
        if (len(right_node)) > 0:
            print(f'Potential rights {right_node}')
            known_right = [item for item in to_ignore if item.x == right_node[0].x and item.y == right_node[0].y]
            if len(known_right) == 0 or right_node[0].key == start_node.key:
                print(f'Right found {right_node[0]}')
                to_ignore.append(right_node[0])
                steps += 1
                return count_steps_to_start(right_node[0], nodes, steps, start_node, False, to_ignore)
            else:
                print(f'Right is already known and is not start')
        else:
            print(f'No right node, stopping')
    if current_node.key == '|':
        top_node = [item for item in nodes if item.x == current_node.x and item.y == current_node.y - 1]
        if (len(top_node)) > 0 and (top_node[0].key == '|' or top_node[0].key == '7' or top_node[0].key == 'F'):
            known_top = [item for item in to_ignore if item.x == top_node[0].x and item.y == top_node[0].y]
            if len(known_top) == 0 or top_node[0].key == start_node.key:
                print(f'Top found {top_node[0]}')
                to_ignore.append(top_node[0])
                steps += 1
                return count_steps_to_start(top_node[0], nodes, steps, start_node, False, to_ignore)
            else:
                print(f'Top is already known and is not start')
        else:
            print(f'No top node, stopping')
        bottom_node = [item for item in nodes if item.x == current_node.x and item.y == current_node.y + 1]
        if (len(bottom_node)) > 0 and (
                bottom_node[0].key == '|' or bottom_node[0].key == 'J' or bottom_node[0].key == 'L'):
            known_bottom = [item for item in to_ignore if item.x == bottom_node[0].x and item.y == bottom_node[0].y]
            if len(known_bottom) == 0 or bottom_node[0].key == start_node.key:
                print(f'Bottom found {bottom_node[0]}')
                to_ignore.append(bottom_node[0])
                steps += 1
                return count_steps_to_start(bottom_node[0], nodes, steps, start_node, False, to_ignore)
            else:
                print(f'Bottom is already known and is not start')
        else:
            print(f'No bottom node, stopping')
    if current_node.key == 'F':
        right_node = [item for item in nodes if item.x == current_node.x + 1 and item.y == current_node.y and (
                item.key == '-' or item.key == 'J' or item.key == '7')]
        if (len(right_node)) > 0:
            print(f'Potential rights {right_node}')
            known_right = [item for item in to_ignore if item.x == right_node[0].x and item.y == right_node[0].y]
            if len(known_right) == 0 or right_node[0].key == start_node.key:
                print(f'Right found {right_node[0]}')
                to_ignore.append(right_node[0])
                steps += 1
                return count_steps_to_start(right_node[0], nodes, steps, start_node, False, to_ignore)
            else:
                print(f'Right is already known and is not start')
        else:
            print(f'No right node, stopping')
        bottom_node = [item for item in nodes if item.x == current_node.x and item.y == current_node.y + 1]
        if (len(bottom_node)) > 0 and (
                bottom_node[0].key == '|' or bottom_node[0].key == 'J' or bottom_node[0].key == 'L'):
            known_bottom = [item for item in to_ignore if item.x == bottom_node[0].x and item.y == bottom_node[0].y]
            if len(known_bottom) == 0 or bottom_node[0].key == start_node.key:
                print(f'Bottom found {bottom_node[0]}')
                to_ignore.append(bottom_node[0])
                steps += 1
                return count_steps_to_start(bottom_node[0], nodes, steps, start_node, False, to_ignore)
            else:
                print(f'Bottom is already known and is not start')
        else:
            print(f'No bottom node, stopping')
    if current_node.key == '7':
        left_node = [item for item in nodes if item.x == current_node.x - 1 and item.y == current_node.y]
        if (len(left_node)) > 0 and (left_node[0].key == '-' or left_node[0].key == 'L' or left_node[0].key == 'F'):
            known_left = [item for item in to_ignore if item.x == left_node[0].x and item.y == left_node[0].y]
            if len(known_left) == 0 or known_left[0].key == start_node.key:
                print(f'Left found {left_node[0]}')
                to_ignore.append(left_node[0])
                steps += 1
                return count_steps_to_start(left_node[0], nodes, steps, start_node, False, to_ignore)
            else:
                print(f'Left is already known and is not start')
        else:
            print(f'No left node, stopping')
        bottom_node = [item for item in nodes if item.x == current_node.x and item.y == current_node.y + 1]
        if (len(bottom_node)) > 0 and (
                bottom_node[0].key == '|' or bottom_node[0].key == 'J' or bottom_node[0].key == 'L'):
            known_bottom = [item for item in to_ignore if item.x == bottom_node[0].x and item.y == bottom_node[0].y]
            if len(known_bottom) == 0 or bottom_node[0].key == start_node.key:
                print(f'Bottom found {bottom_node[0]}')
                to_ignore.append(bottom_node[0])
                steps += 1
                return count_steps_to_start(bottom_node[0], nodes, steps, start_node, False, to_ignore)
            else:
                print(f'Bottom is already known and is not start')
        else:
            print(f'No bottom node, stopping')
    if current_node.key == 'L':
        right_node = [item for item in nodes if item.x == current_node.x + 1 and item.y == current_node.y and (
                item.key == '-' or item.key == 'J' or item.key == '7')]
        if (len(right_node)) > 0:
            print(f'Potential rights {right_node}')
            known_right = [item for item in to_ignore if item.x == right_node[0].x and item.y == right_node[0].y]
            if len(known_right) == 0 or right_node[0].key == start_node.key:
                print(f'Right found {right_node[0]}')
                to_ignore.append(right_node[0])
                steps += 1
                return count_steps_to_start(right_node[0], nodes, steps, start_node, False, to_ignore)
            else:
                print(f'Right is already known and is not start')
        else:
            print(f'No right node, stopping')
        top_node = [item for item in nodes if item.x == current_node.x and item.y == current_node.y - 1]
        if (len(top_node)) > 0 and (top_node[0].key == '|' or top_node[0].key == '7' or top_node[0].key == 'F'):
            known_top = [item for item in to_ignore if item.x == top_node[0].x and item.y == top_node[0].y]
            if len(known_top) == 0 or top_node[0].key == start_node.key:
                print(f'Top found {top_node[0]}')
                to_ignore.append(top_node[0])
                steps += 1
                return count_steps_to_start(top_node[0], nodes, steps, start_node, False, to_ignore)
            else:
                print(f'Top is already known and is not start')
        else:
            print(f'No top node, stopping')
    if current_node.key == 'J':
        left_node = [item for item in nodes if item.x == current_node.x - 1 and item.y == current_node.y]
        if (len(left_node)) > 0 and (left_node[0].key == '-' or left_node[0].key == 'L' or left_node[0].key == 'F'):
            known_left = [item for item in to_ignore if item.x == left_node[0].x and item.y == left_node[0].y]
            if len(known_left) == 0 or known_left[0].key == start_node.key:
                print(f'Left found {left_node[0]}')
                to_ignore.append(left_node[0])
                steps += 1
                return count_steps_to_start(left_node[0], nodes, steps, start_node, False, to_ignore)
            else:
                print(f'Left is already known and is not start')
        else:
            print(f'No left node, stopping')
        top_node = [item for item in nodes if item.x == current_node.x and item.y == current_node.y - 1]
        if (len(top_node)) > 0 and (top_node[0].key == '|' or top_node[0].key == '7' or top_node[0].key == 'F'):
            known_top = [item for item in to_ignore if item.x == top_node[0].x and item.y == top_node[0].y]
            if len(known_top) == 0 or top_node[0].key == start_node.key:
                print(f'Top found {top_node[0]}')
                to_ignore.append(top_node[0])
                steps += 1
                return count_steps_to_start(top_node[0], nodes, steps, start_node, False, to_ignore)
            else:
                print(f'Top is already known and is not start')
        else:
            print(f'No top node, stopping')
    return steps

