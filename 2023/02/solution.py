import re


def open_file():
    file = open("puzzle.txt", "r")
    return file.read().split('\n')


def find_digit(txt):
    return int(re.findall(r'\d+', txt)[0])


class Set:
    red: 0
    green: 0
    blue: 0

    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

lines = open_file()
game_id = 0
games = []

for line in lines:

    game_sets = []
    game_id += 1
    sets_of_cubes = line.split(':')[1].split(';')

    for sets in sets_of_cubes:
        r = g = b = 0
        for cube in sets.split(','):
            if cube.__contains__('red'):
                r = find_digit(cube)
            if cube.__contains__('green'):
                g = find_digit(cube)
            if cube.__contains__('blue'):
                b = find_digit(cube)
        game_sets.append(Set(r, g, b))
    games.append({game_id: game_sets})

ids = []

# part I

for game in games:
    blues = greens = reds = 0
    for v in game.values():
        is_valid = True

        for x in v:
            if x.red > 12:
                is_valid = False
                break
            if x.green > 13:
                is_valid = False
                break
            if x.blue > 14:
                is_valid = False
                break
        if is_valid:
            ids.append(list(game.keys())[0])

print(sum(ids))

# part II

powers = []

for game in games:
    max_red = max_green = max_blue = 0
    for values_set in game.values():
        for item in values_set:
            if item.red > max_red:
                max_red = item.red

            if item.green > max_green:
                max_green = item.green

            if item.blue > max_blue:
                max_blue = item.blue

    power = max_red * max_green * max_blue
    powers.append(power)


print(sum(powers))


