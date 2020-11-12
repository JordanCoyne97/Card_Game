import numpy as np
import random

picture = {
    "Jack": 11,
    "Queen": 12,
    "King": 13,
    "Ace": 14,
}
suitColor = {
 'Hearts': 'red',
 'Clubs': 'black',
 'Diamonds': 'red',
 'Spades':'black'
}

class Card:

    def __init__(self, no, suit):
        self.no = no
        self.suit = suit
        self.value = self.no
        if(no in picture):
            self.valuevalue = picture[no]
        self.color = suitColor[suit]



    def getCard(self):
         print(self.no + " of " + self.suit)

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

    def __gt__(self, other):
        if(self.value > other.value):
            return True
        else:
            return False

    def __lt__(self, other):
        if(self.value < other.value):
            return True
        else:
            return False

def maxCard(card1, card2):
    if card1 >= card2:
        return card1
    else:
        return card2
def minCard(card1, card2):
    if card1 <=card2:
        return card1
    else:
        return card2




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


def initDeck():
    numbers = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']
    suits = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
    deck = [Card(n, s) for s in suits for n in numbers]
    return deck


def run(deck):
    hand = random.sample(deck, 4)

    redOrBlack = input("Red or Black: ").lower()
    if(redOrBlack != hand[0].color):
        hand[0].getCard()
        return "DRINK"

    hand[0].getCard()

    highOrLow = input("Higher or Lower: ").lower()
    if (highOrLow=="higher" and hand[0] > hand[1]) or (highOrLow =="lower" and hand[0] < hand[1]):
        hand[1].getCard()
        return "Drink"

    hand[1].getCard()

    highCard = maxCard(hand[0], hand[1])
    lowCard = minCard(hand[0], hand[1])
    inOrOut = input("Inside or Outside: ").lower()

    if inOrOut=="ouside"  and ( hand[2] in range(lowCard, highCard) ):
        hand[2].getCard()
        return "Drink"
    elif inOrOut=="Inside" and  not( hand[2] in range(lowCard, highCard)):
        hand[2].getCard();
        return "Drink"

    hand[2].getCard()

    suitGuess = input("Guess the Suit: ").lower()
    if(suitGuess != hand[3].suit):
        hand[3].getCard()
        return "Drink"

    hand[3].getCard()
    print("SUCCESS")

def main():
    deck = initDeck()
    # while get_king_count() != 0:
    #     get_king_count()
    #     input = input('Testing')
    # for card in deck:
    #     print(card.getCard())

    #test inequality
    # if(deck[10] >= deck[9]):
    #     print("Hit")

    # print(deck[10].color)
    result = run(deck)
    print(result)

main()
