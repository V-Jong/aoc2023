from itertools import combinations


class Planet:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'({self.x}, {self.y})'


class EmptySpace:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'({self.x}, {self.y})'


def do_challenge():
    file = open('11/input.txt', 'r')
    lines = file.read().splitlines()

    planets = []
    empty_spaces = []
    for line_index, line in enumerate(lines):
        line_chars = [*line]
        for c_index, char in enumerate(line_chars):
            if char == '#':
                planets.append(Planet(c_index, line_index))
            if line_index == 0:
                all_space = True
                for i in range(0, len(lines), 1):
                    line_at_index = lines[i]
                    if line_at_index[c_index] != '.':
                        all_space = False
                        break
                if all_space:
                    empty_spaces.append(EmptySpace(c_index, -1))

        if all(space == '.' for space in line_chars):
            empty_spaces.append(EmptySpace(-1, line_index))

    print(f'{planets}')
    print(f'{empty_spaces}')
    combs = combinations(planets, 2)
    distance = 0
    distance_enhancer = 1000000 - 1
    for comb in combs:
        # print(f'Checking planet {comb[0]} - {comb[1]}')
        planet1x = comb[0].x
        planet1y = comb[0].y
        planet2x = comb[1].x
        planet2y = comb[1].y
        x_distance = abs(planet1x - planet2x)
        y_distance = abs(planet1y - planet2y)
        empty_spaces_between = [s for s in empty_spaces if
                                (planet1x < s.x < planet2x or planet2x < s.x < planet1x) or
                                (planet1y < s.y < planet2y or planet2y < s.y < planet1y)]
        # print(f'Found empty spaces: {empty_spaces_between}')
        distance_to_add = x_distance + y_distance + distance_enhancer * len(empty_spaces_between)
        # print(f'Distance {distance_to_add}')
        distance += distance_to_add
    print(f'Distance: {distance}')
