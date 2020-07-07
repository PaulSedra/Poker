from poker.validators import StraightValidator

class StraightFlushValidator(StraightValidator):
    def __init__(self, cards):
        self._cards = cards
        self._name = 'Straight Flush'

    def __gt__(self, other):
        return self.valid_cards()[-1].rank_index > other.valid_cards()[-1].rank_index

    def is_valid(self):
        return len(self._collections_of_five_straight_cards_in_a_row_of_the_same_suit) >= 1

    def valid_cards(self):
        return self._collections_of_five_straight_cards_in_a_row_of_the_same_suit[-1]

    @property
    def _collections_of_five_straight_cards_in_a_row_of_the_same_suit(self):
        return [
            five_cards
            for five_cards in self._collections_of_five_straight_cards_in_a_row
            if len({ card.suit for card in five_cards }) == 1
        ]