file = open('17/test.txt', 'r')
lines = file.read().splitlines()

grid = {}
path = {}


def do_challenge():
    max_x = 0
    for l_index, line in enumerate(lines):
        separated = [*line]
        if max_x == 0:
            max_x = len(separated) - 1
        for s_index, s in enumerate(separated):
            grid.update({(s_index, l_index): int(s)})
    max_y = len(lines) - 1

    find_path((0, 0), 'down', max_x, max_y)
    print_debug()


def find_path(current_node: (int, int), direction: str, max_x: int, max_y: int):
    stack = [(current_node, direction, 0)]

    while stack:
        current_node, direction, weight = stack.pop()
        print(f'\nChecking current: {current_node}')
        if current_node[0] == max_x and current_node[1] == max_y:
            print(f'Reached target!')
            break
        path.update({current_node: grid.get(current_node)})

        # Get neighbours
        if direction == 'up' or direction == 'down':
            u_neighbours = []
            r_neighbours = [(node, weight) for node, weight in grid.items() if node[1] == current_node[1] and
                            (node[0] == current_node[0] + 1 or node[0] == current_node[0] + 2 or node[0] ==
                             current_node[0] + 3) and node not in path]
            l_neighbours = [(node, weight) for node, weight in grid.items() if node[1] == current_node[1] and
                            (node[0] == current_node[0] - 1 or node[0] == current_node[0] - 2 or node[0] ==
                             current_node[0] - 3) and node not in path]
            d_neighbours = []
        else:
            u_neighbours = [(node, weight) for node, weight in grid.items() if node[0] == current_node[0] and
                            (node[1] == current_node[1] - 1 or node[1] == current_node[1] - 2 or node[1] ==
                             current_node[1] - 3) and node not in path]
            r_neighbours = []
            l_neighbours = []
            d_neighbours = [(node, weight) for node, weight in grid.items() if node[0] == current_node[0] and
                            (node[1] == current_node[1] + 1 or node[1] == current_node[1] + 2 or node[1] ==
                             current_node[1] + 3) and node not in path]
        neighbours = u_neighbours + r_neighbours + l_neighbours + d_neighbours
        # print(f'Neighbours: {neighbours}')

        # Get cheapest neighbour
        if len(neighbours) == 0:
            print(f'No neighbours found, stopping...')
            break
        cheapest = min(neighbours, key=lambda n: n[1])
        all_cheapest = [(node, weight) for node, weight in neighbours if weight == cheapest[1]]
        print(f'All cheapest: {all_cheapest}')
        if len(all_cheapest) > 1:
            all_cheapest = [all_cheapest[0]]

        if len(all_cheapest) == 1 and not all_cheapest[0][0] in path:
            cheapest_one = all_cheapest[0]
            cheapest_one_coord = all_cheapest[0][0]
            cheapest_direction = ''
            if current_node[0] == cheapest_one_coord[0]:
                if current_node[1] < cheapest_one_coord[1]:
                    cheapest_direction = 'down'
                else:
                    cheapest_direction = 'up'
            if current_node[1] == cheapest_one_coord[1]:
                if current_node[0] < cheapest_one_coord[0]:
                    cheapest_direction = 'right'
                else:
                    cheapest_direction = 'left'
            print(f'Cheapest neighbours has weight: {cheapest_one} going {cheapest_direction}')
            # add all to path that have been jumped over
            if cheapest_direction == 'right':
                skipped = [(node, weight) for node, weight in neighbours if
                           current_node[0] < node[0] < cheapest_one_coord[0]]
            if cheapest_direction == 'down':
                skipped = [(node, weight) for node, weight in neighbours if
                           current_node[1] < node[1] < cheapest_one_coord[1]]
            if cheapest_direction == 'up':
                skipped = [(node, weight) for node, weight in neighbours if
                           current_node[1] > node[1] > cheapest_one_coord[1]]
            if cheapest_direction == 'left':
                skipped = [(node, weight) for node, weight in neighbours if
                           current_node[0] > node[0] > cheapest_one_coord[0]]
            print(f'Adding skipped to path: {skipped}')
            for s in skipped:
                path.update({s[0]: s[1]})
            stack.append((cheapest_one[0], cheapest_direction, cheapest_one[1]))
        else:
            print(f'Cheapest {all_cheapest[0]} already in path')


def print_debug():
    open('17/debug.txt', 'w').close()
    with open("17/debug.txt", "a") as f:
        for l_index, line in enumerate(lines):
            n_line = ''
            for c_index, c in enumerate(line):
                if any(pn for pn in path.keys() if pn[0] == c_index and pn[1] == l_index):
                    n_line += '#'
                else:
                    n_line += '.'
            print(f'{n_line}', file=f)
        print('')
