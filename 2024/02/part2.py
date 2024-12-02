def is_safe_report(report: []):

    is_increasing = report == sorted(report)
    is_decreasing = report == sorted(report, reverse=True)

    for i in range(len(report) - 1):
        first = report[i]
        second = report [i + 1]
        difference = abs(first - second)

        if difference < 1 or difference > 3:
            return False

    return is_decreasing or is_increasing

def is_fixable(report):
    for i in range(0, len(report)):
        cursor = report[:i] + report[i + 1:]
        if is_safe_report(cursor):
            return True


with open('puzzle.txt') as file:
    puzzles = file.read().split('\n')
    result = 0

    for puzzle in puzzles:
        reports = [int(x) for x in puzzle.split()]

        if is_fixable(reports):
            result += 1

    print(f'Result: {result}')
