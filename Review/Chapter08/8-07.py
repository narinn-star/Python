import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def getRank(self):
        return self.rank
    
    def getSuit(self):
        return self.suit

class Deck:
    '52 카드의 카드 덱 표현'
    ranks = {'2','3','4','5','6','7','8','9','10','J','Q','K','A'}

    suits = {'\u2660', '\u2661', '\u2662', '\u2663'}

    def __init__(self, cardList = None):
        self.cards = list()
        for suit in Deck.suits:
            for rank in Deck.ranks:
                self.cards.append(Card(rank, suit))

    def dealCard(self):
        return self.cards.pop(0)
    
    def shuffle(self):
        random.shuffle(self.cards)