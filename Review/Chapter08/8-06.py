class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def getRank(self):
        return self.rank
    
    def getSuit(self):
        return self.suit
    
    def __repr__(self):
        return "Card('{}', '{}')".format(self.rank, self.suit)

    def __eq__(self, other):
        return self.suit == other.suit and self.rank == other.rank

Card('3', '\u2660') == Card('3', '\u2660')
#True

Card('3', '\u2660') == eval(repr(Card('3', '\u2660')))
#True