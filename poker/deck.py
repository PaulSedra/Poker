import random

class Deck():
    def __init__(self):
        self._cards = []

    def __len__(self):
        return len(self._cards)

    @property
    def cards(self):
        return self._cards

    def add_cards(self, cards):
        self._cards.extend(cards)
    
    def remove_cards(self, number):
        return [self._cards.pop(0) for _ in range(number)]

    def shuffle(self):
        random.shuffle(self._cards)
