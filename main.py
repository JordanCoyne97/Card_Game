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
            self.value = picture[no]
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

    if inOrOut=="outside"  and ( hand[2].value in range(lowCard.value, highCard.value) ):
        hand[2].getCard()
        return "Drink"
    elif inOrOut=="Inside" and  not( hand[2].value in range(lowCard.value, highCard.value)):
        hand[2].getCard();
        return "Drink"

    hand[2].getCard()

    suitGuess = input("Guess the Suit: ").lower()
    if(suitGuess != hand[3].suit.lower()):
        hand[3].getCard()
        return "Drink"

    hand[3].getCard()
    return "Success"


def play_round():
    deck = initDeck()

    result = run(deck)
    print(result)
    main()


def main():
    choice = input("play another round? y/n: ")
    print("Starting game ...\n")

    if choice == "y":
        play_round()
    else:
        return


main()
