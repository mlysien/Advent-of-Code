import re


def open_file():
    file = open("puzzle.txt", "r")
    return file.read().split('\n')


def is_digit(txt):
    return int(re.findall(r'\d+', txt)[0])


class Element:
    number: int
    gear_x: int
    gear_y: int
    gear_symbol: str
    is_part: bool

    def __init__(self, number: int, is_part: bool, gear_symbol: str, gear_x: int, gear_y: int):
        self.number = number
        self.is_part = is_part
        self.gear_symbol = gear_symbol
        self.gear_x = gear_x
        self.gear_y = gear_y


lines = open_file()

schema = []
for line in lines:
    row = []
    for symbol in line:
        row.append(symbol)
    schema.append(row)

elements = []

for y, row in enumerate(schema):
    digits = ''
    for x, symbol in enumerate(row):

        number = 0
        if symbol.isdigit():
            digits += symbol

        if (not symbol.isdigit() and not digits == '') or (x == len(row) - 1 and symbol.isdigit()):
            number = int(digits)
            is_part = False
            gear_symbol = ''
            gear_x = gear_y = 0
            for i in range(len(digits) + 2):
                current = schema[y][x - i]
                top = schema[y - 1 if y - 1 >= 0 else 0][x - i if x - i >= 0 else 0]
                bottom = schema[y + 1 if y + 1 < len(schema) else len(schema) - 1][x - i if x - i >= 0 else 0]

                if not current.isdigit() and not current == '.':
                    gear_symbol = current
                    gear_x = x - i
                    gear_y = y
                    is_part = True
                    break

                if not top.isdigit() and not top == '.':
                    gear_symbol = top
                    gear_x = x - i if x - i >= 0 else 0
                    gear_y = y - 1 if y - 1 >= 0 else 0
                    is_part = True
                    break

                if not bottom.isdigit() and not bottom == '.':
                    gear_symbol = bottom
                    gear_x = x - i if x - i >= 0 else 0
                    gear_y = y + 1 if y + 1 < len(schema) else len(schema) - 1
                    is_part = True
                    break

            digits = ''
            elements.append(Element(number, is_part, gear_symbol, gear_x, gear_y))

        if not symbol.isdigit() and not symbol == '.':
            continue

s = 0
for index, element in enumerate([s for s in elements if s.gear_symbol == '*']):
    for ratio in [s for s in elements if s.gear_symbol == '*'][index+1:]:
        if ratio.gear_x == element.gear_x and ratio.gear_y == element.gear_y:
            s += element.number * ratio.number

print(s)

