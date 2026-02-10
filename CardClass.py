import random

ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        if(rank == 'J' or rank == 'Q' or rank == 'K'):
            self.value = 10
        elif(rank == 'A'):  
            self.value = 1
        else:
            self.value = int(rank)

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:

    def __init__( self ):
        self.contents = []
        self.contents = [ Card( rank, suit ) for rank in ranks for suit in suits ]
        random.shuffle( self.contents )


class Hand:
    def __init__(self, deck):
        self.cards = []
        for i in range(4):
            self.cards.append(deck.contents.pop())

    def __str__(self):
        return ', '.join(str(card) for card in self.cards)
        


def fifteens(handInd, cur_val):
    val = cur_val
    val += hand[handInd]

    if(val < 15):
        handInd+=1
        fifteens(handInd, val)
    else:
        pass

player1 = Hand(Deck())
print(player1)
