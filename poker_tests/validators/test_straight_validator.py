import unittest

from poker.card import Card
from poker.validators import StraightValidator

# results in error (refer to call documentation)
# cards = [
#     Card(rank='2', suit='Hearts'),
#     Card(rank='6', suit='Hearts'),
#     self.seven_of_diamonds,
#     self.eight_of_spades,
#     self.nine_of_clubs,
#     self.ten_of_diamonds,
#     self.jack_clubs
# ]

class StraightValidatorTest(unittest.TestCase):
    def setUp(self):
        self.seven_of_diamonds = Card(rank='7', suit='Diamonds')
        self.eight_of_spades = Card(rank='8', suit='Spades')
        self.nine_of_clubs = Card(rank='9', suit='Clubs')
        self.ten_of_diamonds = Card(rank='10', suit='Diamonds')
        self.jack_clubs = Card(rank='Jack', suit='Clubs')

        self.cards = [
            Card(rank='2', suit='Hearts'),
            Card(rank='6', suit='Hearts'),
            self.seven_of_diamonds,
            self.eight_of_spades,
            self.nine_of_clubs,
            self.ten_of_diamonds,
            self.jack_clubs
        ]

    def test_validates_that_cards_have_five_consecutive_card_in_rank(self):
        validator = StraightValidator(cards=self.cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_does_not_deem_two_consecutive_cards_as_straight(self):
        cards = [
            Card(rank='6', suit='Hearts'),
            Card(rank='7', suit='Hearts')
        ]

        validator = StraightValidator(cards=cards)

        self.assertEqual(
            validator.is_valid(),
            False
        )

    def test_returns_highest_straight_cards_from_card_collection(self):
        validator = StraightValidator(cards=self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
            self.seven_of_diamonds,
            self.eight_of_spades,
            self.nine_of_clubs,
            self.ten_of_diamonds,
            self.jack_clubs
            ]
        )

    def test_considers_a_straight_greater_than_another_by_comparing_the_last_card_in_both_straights(self):
        other_cards = [
            Card(rank='5', suit='Hearts'),
            Card(rank='6', suit='Clubs'),
            Card(rank='7', suit='Diamonds'),
            Card(rank='8', suit='Hearts'),
            Card(rank='9', suit='Spades')
        ]

        validator1 = StraightValidator(cards=self.cards)
        validator2 = StraightValidator(cards=other_cards)

        self.assertEqual(
            validator1 > validator2,
            True
        )