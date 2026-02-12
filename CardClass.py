import random

ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
# This file will contain the classes for the cards, deck, hand, and player. 
# It will also contain the functions for calculating the score of a hand and the crib. 
# The functions for calculating the score of a hand and the crib will be based on the rules of cribbage.
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
    
def Player():
    def __init__(self, name):
        self.name = name
        self.hand = Hand(Deck())
        self.score = 0
        self.cur_hand_val = 0 

    def calculate_score(self):
        self.cur_hand_val += fifteens(self.hand.cards, 0, 0)
        self.score += self.cur_hand_val

    def __str__(self):
        return self.name + " has the hand: " + str(self.hand) + " and a score of: " + str(self.score)
        
def throw_pile():

    def __init__(self, owner_name):
        # This class will represent the pile of cards that a player has thrown in for the crib.
        #  It will be used to calculate the score of the crib and to determine which cards are in the crib.
        self.owner_name = owner_name
        self.cards = [] 

def fifteens(hand, handInd, cur_val):
    val = cur_val
    val += hand[handInd]

    if(val < 15):
        handInd+=1
        fifteens(hand, handInd, val)
    else:
        pass

player1 = Player("Alice")
print(player1)

hand = [card.value for card in player1.cards]
fifteens(hand, 0, 0)
