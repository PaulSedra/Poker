from poker.validators import SameRankValidator, ThreeOfAKindValidator

class FullHouseValidator(SameRankValidator):
    def __init__(self, cards):
        self._cards = cards
        self._name = 'Full House'

    def __gt__(self, other):
        if self.three_of_a_kind_cards[-1].rank_index == other.three_of_a_kind_cards[-1].rank_index:
            return self.pair_cards[-1].rank_index > other.pair_cards[-1].rank_index
        return self.three_of_a_kind_cards[-1].rank_index > other.three_of_a_kind_cards[-1].rank_index

    def is_valid(self):
        return ThreeOfAKindValidator(cards=self._cards).is_valid() and len(self._ranks_with_count(2)) > 0

    def valid_cards(self):
        three_of_a_kind_cards = self.three_of_a_kind_cards
        pair_cards = self.pair_cards
        all_cards = three_of_a_kind_cards + pair_cards
        all_cards.sort()
        return all_cards

    @property
    def three_of_a_kind_cards(self):
        return ThreeOfAKindValidator(cards=self._cards).valid_cards()

    @property
    def pair_cards(self):
        return [card for card in self._cards if card.rank in self._ranks_with_count(2).keys()][-2:]