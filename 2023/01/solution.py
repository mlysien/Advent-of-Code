def open_puzzle():
    file = open("puzzle.txt", "r")
    return file.read().split('\n')


puzzle = open_puzzle()
calibration_values = 0
digits = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}


for line in puzzle:
    # 3two3eightjszbfourkxbh5twonepr

    digits_indexes = []

    first_digit = last_digit = 0

    for c in line:
        if c.isdigit():
            first_digit = int(c)
            index = line.find(c)
            digits_indexes.append({index: int(c)})
            break

    for digit in digits:
        index = line.find(digit)
        if index >= 0:
            digits_indexes.append({index: int(digits[digit])})

    for c in line[::-1]:
        if c.isdigit():
            last_digit = int(c)
            index = line.rfind(c)
            if index >= 0:
                if digits_indexes.__contains__({index: int(c)}):
                    continue
                else:
                    digits_indexes.append({index: int(c)})
            break

    for digit in digits:
        index = line.rfind(digit)
        if index >= 0:
            if digits_indexes.__contains__({index: int(digits[digit])}):
                continue
            else:
                digits_indexes.append({index: int(digits[digit])})

    min_key = 100000
    max_key = 0
    for x in digits_indexes:
        key = min(x.keys())
        if key < min_key:
            min_key = key
    for x in digits_indexes:
        key = max(x.keys())
        if key > max_key:
            max_key = key

    num1 = num2 = 0
    for dictionary in digits_indexes:
        t = list(dictionary.keys())[0]
        if list(dictionary.keys())[0] == min_key:
            num1 = list(dictionary.values())[0]
            break

    for dictionary in digits_indexes:
        t = list(dictionary.keys())[0]
        if list(dictionary.keys())[0] == max_key:
            num2 = list(dictionary.values())[0]
            break

    if num2 == 0:
        print(line)

    calibration_values += int(f'{num1}{num2}')

print(f'Sum of all of the calibration values is {calibration_values}')

