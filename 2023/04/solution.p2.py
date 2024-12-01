def open_file():
    file = open("puzzle.txt", "r")
    return file.read().split('\n')


cards = open_file()
winning_numbers = []
my_numbers = []
scratchcards = {}

for current_card, card in enumerate(cards):

    if current_card not in scratchcards:
        scratchcards[current_card] = 1

    winning_numbers = [n for n in card.split(':')[1].split('|')[0].strip().split(' ') if n]
    my_numbers = [n for n in card.split(':')[1].split('|')[1].strip().split(' ') if n]
    matching_cards = 0

    for luck in my_numbers:
        if winning_numbers.__contains__(luck):
            matching_cards += 1

    for next_card in range(current_card + 1, current_card + matching_cards + 1):
        scratchcards[next_card] = scratchcards.get(next_card, 1) + scratchcards[current_card]

print(f'Total scratchcards: {sum(scratchcards.values())}')
