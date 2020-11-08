import numpy as np


def card_count_left_in_deck():
    return len(deck)


def get_king_count():
    return np.count_nonzero(deck == 'King')


values = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
suites = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
deck = [[v + ' of ' + s] for s in suites for v in values]


def main():
    while get_king_count() != 0:
        get_king_count()
        input = input('Testing')


main()