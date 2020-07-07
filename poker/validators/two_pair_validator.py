from poker.validators import SameRankValidator

class TwoPairValidator(SameRankValidator):
    def __init__(self, cards):
        self._cards = cards
        self._name = 'Two Pair'

    def __gt__(self, other):
        if self.valid_cards()[-1].rank_index == other.valid_cards()[-1].rank_index:
            return self.valid_cards()[-3].rank_index > other.valid_cards()[-3].rank_index
        return self.valid_cards()[-1].rank_index > other.valid_cards()[-1].rank_index

    def is_valid(self):
        return len(self._ranks_with_count(2)) >= 2

    def valid_cards(self):
        ranks_with_pairs = self._ranks_with_count(2)
        return [card for card in self._cards if card.rank in ranks_with_pairs.keys()]