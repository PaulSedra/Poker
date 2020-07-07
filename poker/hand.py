from poker.validators import (
    RoyalFlushValidator,
    StraightFlushValidator,
    FourOfAKindValidator,
    FullHouseValidator,
    FlushValidator,
    StraightValidator,
    ThreeOfAKindValidator,
    TwoPairValidator,
    PairValidator,
    HighCardValidator,
    NoCardsValidator
)

class Hand():
    VALIDATORS = (
        RoyalFlushValidator,
        StraightFlushValidator,
        FourOfAKindValidator,
        FullHouseValidator,
        FlushValidator,
        StraightValidator,
        ThreeOfAKindValidator,
        TwoPairValidator,
        PairValidator,
        HighCardValidator,
        NoCardsValidator
    )

    def __init__(self):
        self._cards = []
        self._validator = None

    def __repr__(self):
        card_as_strings = [str(card) for card in self._cards]
        return ', '.join(card_as_strings)

    def add_cards(self, cards):
        copy = self._cards[:]
        copy.extend(cards)
        copy.sort()
        self._cards = copy

    @property
    def cards(self):
        return self._cards

# ! add test class
    @cards.setter
    def cards(self, cards):
        self._cards = cards

    def best_rank(self):
        for index, validator in enumerate(self.VALIDATORS):
            if validator(cards=self._cards).is_valid():
                best_rank = validator(cards=self._cards)
                self._validator = validator
                return (index, best_rank._name, best_rank.valid_cards())