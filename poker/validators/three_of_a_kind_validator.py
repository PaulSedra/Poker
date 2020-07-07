from poker.validators import SameRankValidator

class ThreeOfAKindValidator(SameRankValidator):
    def __init__(self, cards):
        self._cards = cards
        self._name = 'Three of a Kind'

    def __gt__(self, other):
        return self.valid_cards()[-1].rank_index > other.valid_cards()[-1].rank_index

    def is_valid(self):
        return len(self._ranks_with_count(3)) == 1

    def valid_cards(self):
        ranks_with_pairs = self._ranks_with_count(3)
        return [card for card in self._cards if card.rank in ranks_with_pairs.keys()]