class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def getRank(self):
        return self.rank
    
    def getSuit(self):
        return self.suit

    def __lt__(self, other):
        return self.rank < other.rank and self.suit < other.suit

    def __gt__(self, other):
        return self.rank > other.rank and self.suit > other.suit

    def __le__(self, other):
        return self.rank <= other.rank and self.suit <= other.suit
    
    def __ge__(self, other):
        return self.rank >= other.rank and self.suit >= other.suit

print('\u2660', '\u2661', '\u2662', '\u2663')

print(Card('3', '\u2660') < Card('8', '\u2662'))
print(Card('3', '\u2660') > Card('8', '\u2662'))
print(Card('3', '\u2660') <= Card('8', '\u2662'))
print(Card('3', '\u2660') >= Card('8', '\u2662'))