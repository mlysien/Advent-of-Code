﻿
if __name__ == '__main__':
    with open('puzzle.txt') as file:
        puzzles = file.read().split('\n')

        left = []
        right = []

        for puzzle in puzzles:
            left.append(int(puzzle.split()[0]))
            right.append(int(puzzle.split()[1]))

        left.sort()
        right.sort()

        puzzles =  [left, right]
        result = 0

        for i in range(0, len(left)):
            result += abs(left[i] - right[i])

        print(f'Result: {result}')
