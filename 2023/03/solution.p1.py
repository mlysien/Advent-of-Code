import re


def open_file():
    file = open("puzzle.txt", "r")
    return file.read().split('\n')


def is_digit(txt):
    return int(re.findall(r'\d+', txt)[0])


class Element:
    number: int
    is_part: bool

    def __init__(self, number: int, is_part: bool):
        self.number = number
        self.is_part = is_part


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

            for i in range(len(digits) + 2):
                current = schema[y][x - i]
                top = schema[y - 1 if y - 1 >= 0 else 0][x - i if x - i >= 0 else 0]
                bottom = schema[y + 1 if y + 1 < len(schema) else len(schema) - 1][x - i if x - i >= 0 else 0]

                if not current.isdigit() and not current == '.':
                    is_part = True
                    break

                if not top.isdigit() and not top == '.':
                    is_part = True
                    break

                if not bottom.isdigit() and not bottom == '.':
                    is_part = True
                    break

            digits = ''
            elements.append(Element(number, is_part))

        if not symbol.isdigit() and not symbol == '.':
            continue

s = 0
for element in elements:
    if element.is_part:
        s += element.number

print(s)
