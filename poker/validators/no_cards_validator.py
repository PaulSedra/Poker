class NoCardsValidator():
    def __init__(self, cards):
        self._cards = cards
        self._name = 'No Cards'

    def is_valid(self):
        return len(self._cards) == 0

    def valid_cards(self):
        return []