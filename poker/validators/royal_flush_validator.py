from poker.validators import StraightFlushValidator

class RoyalFlushValidator():
    def __init__(self, cards):
        self._cards = cards
        self._name = 'Royal Flush'

    def is_valid(self):
        straight_flush_validator = StraightFlushValidator(cards=self._cards)
        if straight_flush_validator.is_valid():
            straight_flush_cards = straight_flush_validator.valid_cards()
            return straight_flush_cards[-1].rank == 'Ace'

        return False

    def valid_cards(self):
        return StraightFlushValidator(cards=self._cards).valid_cards()