import re


class Game:
    def __init__(self, number):
        self.number = number
        self.red = 0
        self.green = 0
        self.blue = 0

    def update_red(self, red):
        self.red = red

    def update_green(self, green):
        self.green = green

    def update_blue(self, blue):
        self.blue = blue

    def is_within_limits(self, game):
        print(f'Comparing {self} to master {game}')
        return self.red <= game.red and self.green <= game.green and self.blue <= game.blue

    def __str__(self):
        return f'Number: {self.number} and red: {self.red}, green: {self.green}, blue: {self.blue}'

    def __repr__(self):
        return f'Number: {self.number} and red: {self.red}, green: {self.green}, blue: {self.blue}'


def do_challenge():
    file = open('2/input.txt', 'r')
    lines = file.readlines()

    master_game = Game(0)
    master_game.update_red(12)
    master_game.update_green(13)
    master_game.update_blue(14)

    games = []
    powers = []
    for line in lines:
        line = line.replace('\n', '')
        game_split = line.split(':')
        game_info = game_split[0]
        game_rolls = game_split[1].strip()  # .split(';')
        print(f'\nParsing game {game_info} with: {game_rolls}')

        game_number = re.findall(r'\d+', game_info)[0]
        game = Game(int(game_number))

        # for game_roll in game_rolls:
            # color_rolls = game_roll.split(',')
            # for color_roll in color_rolls:
            #     color_roll = color_roll.strip()
            #     print(f'roll: {color_roll}')
        red_rolls = list(map(lambda x: int(re.findall(r'\d+', x)[0]), re.findall(r'\d+ red', game_rolls)))
        print(f'Red rolls: {red_rolls}')
        max_red = max(red_rolls)
        print(f'Max Red: {max_red}')
        green_rolls = list(map(lambda x: int(re.findall(r'\d+', x)[0]), re.findall(r'\d+ green', game_rolls)))
        print(f'Green rolls: {green_rolls}')
        max_green = max(green_rolls)
        print(f'Max Green: {max_green}')
        blue_rolls = list(map(lambda x: int(re.findall(r'\d+', x)[0]), re.findall(r'\d+ blue', game_rolls)))
        print(f'Blue rolls: {blue_rolls}')
        max_blue = max(blue_rolls)
        print(f'Max Blue: {max_blue}')
        game.update_red(int(max_red))
        game.update_green(int(max_green))
        game.update_blue(int(max_blue))

        # print(f'Red {max_red}, green {max_green}, blue {max_blue}')

        if game.is_within_limits(master_game):
            games.append(game)

        powers.append(max_red * max_green * max_blue)

    applicable_games = [g.number for g in games]
    print(f'Games: {applicable_games}')
    print(f'Powers: {powers}')
    sum_games = sum(applicable_games)
    sum_powers = sum(powers)
    print(f'Sum of applicable games: {sum_games}')
    print(f'Sum of powers: {sum_powers}')
