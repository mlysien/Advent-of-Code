import re

def mul(x, y):
    return x * y

with open('puzzle.txt') as file:
    memory = file.read()
    instructions = re.findall(r'mul\(\d{1,3},\d{1,3}\)', memory)
    result = 0

    for instruction in instructions:
        digits = [int(s) for s in re.findall(r'\b\d+\b', instruction)]
        result += mul(digits[0], digits[1])

    print(f'Result: {result}')
