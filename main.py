import numpy as np


def card_count_left_in_deck():
    return len(deck)


def get_king_count():
    counter = 0

    for card in deck:
        if card == 'King of Hearts' or card == 'King of Spades' or card == 'King of Diamonds' or card == 'King of Clubs':
            counter = counter + 1
            print('found')

    if 'King of Hearts' in deck:
        counter = counter + 1

    return counter


values = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
suites = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
deck = [[v + ' of ' + s] for s in suites for v in values]


def main():
    while get_king_count() != 0:
        get_king_count()
        input = input('Testing')


main()