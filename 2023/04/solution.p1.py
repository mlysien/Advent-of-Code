def open_file():
    file = open("puzzle.txt", "r")
    return file.read().split('\n')


lines = open_file()
winning_numbers = []
my_numbers = []
total_points = 0

for line in lines:
    winning_numbers = [n for n in line.split(':')[1].split('|')[0].strip().split(' ') if n]
    my_numbers = [n for n in line.split(':')[1].split('|')[1].strip().split(' ') if n]
    points = 0
    for luck in my_numbers:
        if winning_numbers.__contains__(luck):
            points += 1

    if points > 0:
        total_points += 2**(points-1)

print(f'Total points: {total_points}')
