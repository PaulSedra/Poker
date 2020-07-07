import unittest

from poker.card import Card
from poker.validators import StraightFlushValidator

class StraightFlushValidatorTest(unittest.TestCase):
    def setUp(self):
        self.three_of_clubs = Card(rank='3', suit='Clubs')
        self.four_of_clubs = Card(rank='4', suit='Clubs')
        self.five_of_clubs = Card(rank='5', suit='Clubs')
        self.six_of_clubs = Card(rank='6', suit='Clubs')
        self.seven_of_clubs = Card(rank='7', suit='Clubs')

        self.cards = [
            self.three_of_clubs,
            self.four_of_clubs,
            self.five_of_clubs,
            self.six_of_clubs,
            self.seven_of_clubs,
            Card(rank='King', suit='Clubs'),
            Card(rank='Ace', suit='Diamonds')
        ]

    def test_validates_that_cards_do_not_have_five_consecutive_cards_of_the_same_suit(self):
        cards = [
            self.three_of_clubs,
            self.four_of_clubs,
            self.five_of_clubs,
            self.six_of_clubs,
            Card(rank='7', suit='Diamonds'),
            Card(rank='King', suit='Clubs'),
            Card(rank='Ace', suit='Diamonds')
        ]

        validator = StraightFlushValidator(cards=cards)

        self.assertEqual(
            validator.is_valid(),
            False
        )

    def test_validates_that_cards_have_five_consecutive_cards_of_the_same_suit(self):
        validator = StraightFlushValidator(cards=self.cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_five_consecutive_cards_of_the_same_suit_from_card_collection(self):
        validator = StraightFlushValidator(cards=self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                self.three_of_clubs,
                self.four_of_clubs,
                self.five_of_clubs,
                self.six_of_clubs,
                self.seven_of_clubs
            ]
        )

    def test_considers_a_straight_flush_greater_than_another_by_comparing_the_last_card_in_both_straight_flushes(self):
        other_cards = [
            Card(rank='2', suit='Clubs'),
            self.three_of_clubs,
            self.four_of_clubs,
            self.five_of_clubs,
            self.six_of_clubs,
        ]

        validator1 = StraightFlushValidator(cards=self.cards)
        validator2 = StraightFlushValidator(cards=other_cards)

        self.assertEqual(
            validator1 > validator2,
            True
        )