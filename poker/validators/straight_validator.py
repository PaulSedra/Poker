
# TOFIX: there is a bug if the cards duplicate in the middle
# same with Straight Flush and Royal Flush
# refer to test file for error example

class StraightValidator():
    def __init__(self, cards):
        self._cards = cards
        self._name = 'Straight'

    def __gt__(self, other):
        return self.valid_cards()[-1].rank_index > other.valid_cards()[-1].rank_index

    def is_valid(self):
        return len(self._collections_of_five_straight_cards_in_a_row) >= 1

    def valid_cards(self):
        return self._collections_of_five_straight_cards_in_a_row[-1]

    def _is_consecutive_in_rank(self, rank_indexes):
        return rank_indexes == list(range(rank_indexes[0], rank_indexes[-1] + 1))

    @property
    def _collections_of_five_straight_cards_in_a_row(self):
        index = 0
        final_index = len(self._cards) - 1
        collections_of_five_straight_cards_in_a_row = []

        while index + 4 <= final_index:
            next_five_cards = self._cards[index:index + 5]
            next_five_rank_indices = [card.rank_index for card in next_five_cards]

            if self._is_consecutive_in_rank(next_five_rank_indices):
                collections_of_five_straight_cards_in_a_row.append(next_five_cards)

            index += 1

        return collections_of_five_straight_cards_in_a_row