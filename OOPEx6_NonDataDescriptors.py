from random import choice

class Choice:
    def __init__(self, *iterable):
        self.iterable = iterable
    
    def __get__(self, instance, owner_class):
        return choice(self.iterable)

class Deck:
    ranks = Choice('Spade', 'Heart', 'Diamond', 'Club')
    suits = Choice(*'23456789JQKA','10')

# card = Deck()

# for _ in range(10):
#     print(card.suits, card.ranks)


class Deck2:
    ranks = ('Spade', 'Heart', 'Diamond', 'Club')
    suits = (*'23456789JQKA','10')

    @staticmethod
    def choices(elem):
        return choice(elem)

card2 = Deck2()

for _ in range(10):
    print(card2.choices(Deck2.suits), card2.choices(Deck2.ranks))
