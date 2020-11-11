import numpy as np

class Card:

    def __init__(self, no, suit):
        self.no = no
        self.suit = suit
        self.value = 0
        if(no == "Ace"):
            self.value = 14
        if(no=="King"):
            self.value = 13
        if(no=="Queen"):
            self.value = 12
        if(no=="Jack"):
            self.value = 11



    def getCard(self):
        return self.no + " of " + self.suit

    def __ge__(self, other):
        if(self.value >= other.value):
            return True
        else:
            return False

    def __le__(self, other):
        if(self.value <= other.value):
            return True
        else:
            return False


# def card_count_left_in_deck():
#     return len(deck)
#
#
# def get_king_count():
#     counter = 0
#
#     for card in deck:
#         if card == 'King of Hearts' or card == 'King of Spades' or card == 'King of Diamonds' or card == 'King of Clubs':
#             counter = counter + 1
#             print('found')
#
#     if 'King of Hearts' in deck:
#         counter = counter + 1
#
#     return counter


numbers = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
suits = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
deck = [Card(n, s) for s in suits for n in numbers]


def main():
    # while get_king_count() != 0:
    #     get_king_count()
    #     input = input('Testing')
    for card in deck:
        print(card.getCard())

    if(deck[10] > deck[9]):
        print("Hit")

main()
