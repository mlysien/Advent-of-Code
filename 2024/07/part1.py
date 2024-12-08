def check_equation(expected_value: int, parameters: list[int]):

    # condition to stop recursive call
    if len(parameters) == 1:
        return expected_value == parameters[0]
    
    last_value = parameters.pop()

    # check if last value is divider of expected value
    if expected_value % last_value == 0:
        if check_equation(expected_value // last_value, parameters.copy()):
            return True

    # check if minus operation is still greater than 0
    if expected_value - last_value > 0:
        if check_equation(expected_value - last_value, parameters.copy()):
            return True

    return False

with open('puzzle.txt', 'r') as puzzle:
    lines = puzzle.read().split('\n')
    result = 0
    for line in lines:
        value = int(line.split(':')[0])
        params = list(map(int, line.split(':')[1].split()))

        if check_equation(value, params.copy()):
            result += value

    print(f'Result: {result}')
