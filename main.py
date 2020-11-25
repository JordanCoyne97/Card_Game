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

class Player:
    def __init__(self, hand, name, drinkAmt = 0):
        self.hand = hand
        self.name = name
        self.drinkAmt = drinkAmt


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

def deal(deck, count):
    hand = []
    for i in range(count):
        index = random.randint(0,len(deck)-1)
        hand.append(deck.pop(index))

    return hand




def run(hand):

    redOrBlack = input("Red or Black: ").lower()
    if(redOrBlack != hand[0].color):
        hand[0].getCard()
        amt = random.randint(2,7)
        return "DRINK"+ str(amt) + "seconds"

    hand[0].getCard()

    highOrLow = input("Higher or Lower: ").lower()
    if (highOrLow=="higher" and hand[0] > hand[1]) or (highOrLow =="lower" and hand[0] < hand[1]):
        hand[1].getCard()
        amt = random.randint(2,7)
        return "DRINK"+ str(amt) + "seconds"

    hand[1].getCard()

    highCard = maxCard(hand[0], hand[1])
    lowCard = minCard(hand[0], hand[1])
    inOrOut = input("Inside or Outside: ").lower()

    if inOrOut=="outside"  and ( hand[2].value in range(lowCard.value, highCard.value) ):
        hand[2].getCard()
        amt = random.randint(2,7)
        return "DRINK"+ str(amt) + "seconds"
    elif inOrOut=="Inside" and  not( hand[2].value in range(lowCard.value, highCard.value)):
        hand[2].getCard();
        amt = random.randint(2,7)
        return "DRINK"+ str(amt) + "seconds"

    hand[2].getCard()

    suitGuess = input("Guess the Suit: ").lower()
    if(suitGuess != hand[3].suit.lower()):
        hand[3].getCard()
        amt = random.randint(7,12)
        return "DRINK"+ str(amt) + "seconds"

    hand[3].getCard()
    amt = random.randint(2,7)
    return "SUCCESS: Give"+ str(amt) + "seconds to somebody"

def pyramid(deck, players):
    rows = []
    for cardCount in range(1,5):
        rows.append(random.sample(deck, cardCount))

    rowDrinkAmt = 0
    for row in rows:
        rowDrinkAmt += 5
        for player in players:
            player.drinkAmt += cardMatch(row, player.hand) * rowDrinkAmt

##card match also removes cards from hands
##we can use set intersetcion becuase cards are unique
def cardMatch(row, hand):

    rowVal = [card.value for card in row]
    handVal = [card.value for card in hand]

    intersect = list(set(rowVal) & set(handVal))

    ## Hand becomes hand/(intersection(hand,Row))
    hand = [card for card in row if card.value not in handVal]

    return len(intersect)

def main():


    deck = initDeck()

    names = ["Tommy","Sillian","d'Oisin"]
    players = []
    for i in names:
        hand = deal(deck, 4)
        players.append( Player( hand, i ) )

    pyramid(deck, players)

    for player in players:
        print(player.name + ": " + str(player.drinkAmt))

    

main()
