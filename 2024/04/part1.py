import re
import numpy as np

def diagonals_rows(matrix):
    a = np.array([list(row) for row in matrix])
    diagonals = [a[::-1, :].diagonal(i) for i in range(-a.shape[0] + 1, a.shape[1])]
    diagonals.extend(a.diagonal(i) for i in range(a.shape[1] - 1, -a.shape[0], -1))
    elements = []
    row = ''

    for diagonal in diagonals:
        for i in range(0, len(diagonal)):
            row += diagonal[i]

        elements.append(row)
        row=''

    return elements

def vertical_rows(matrix: []):
    size = len(matrix[0])
    elements = []
    row = ''

    for index in range(0, size):
        for m in matrix:
            row += m[index]

        elements.append(row)
        row = ''

    return elements


with (open('puzzle.txt') as file):
    word_search = file.read().split('\n')
    pattern = 'XMAS'
    result = 0

    # check horizontal occurrences
    for line in word_search:
        result += len(re.findall(rf'{pattern}', line))
        result += len(re.findall(rf'{pattern}', line[::-1]))

    # check vertical occurrences
    for line in vertical_rows(word_search):
        result += len(re.findall(rf'{pattern}', line))
        result += len(re.findall(rf'{pattern}', line[::-1]))

    # check diagonals occurrences
    for line in diagonals_rows(word_search):
        result += len(re.findall(rf'{pattern}', line))
        result += len(re.findall(rf'{pattern}', line[::-1]))

    print(f'Result: {result}')
