class HighCardValidator():
    def __init__(self, cards):
        self._cards = cards
        self._name = 'High Card'

    def __gt__(self, other):
        return self.valid_cards()[-1].rank_index > other.valid_cards()[-1].rank_index

    def is_valid(self):
        return len(self._cards) >= 1

    def valid_cards(self):
        return self._cards[-1:]