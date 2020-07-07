import unittest

from poker.card import Card
from poker.validators import FourOfAKindValidator

class ThreeOfAKindValidatorTest(unittest.TestCase):
    def setUp(self):
        self.three_of_clubs = Card(rank='3', suit='Clubs')
        self.three_of_diamonds = Card(rank='3', suit='Diamonds')
        self.three_of_hearts = Card(rank='3', suit='Hearts')
        self.three_of_spades = Card(rank='3', suit='Spades')

        self.cards = [
            Card(rank='2', suit='Clubs'),
            self.three_of_clubs,
            self.three_of_diamonds,
            self.three_of_hearts,
            self.three_of_spades,
            Card(rank='7', suit='Hearts'),
            Card(rank='9', suit='Spades')
        ]

    def test_validates_that_cards_have_exactly_four_of_the_same_rank(self):
        validator = FourOfAKindValidator(cards=self.cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_four_of_a_kind_from_card_collection(self):
        validator = FourOfAKindValidator(cards=self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                self.three_of_clubs,
                self.three_of_diamonds,
                self.three_of_hearts,
                self.three_of_spades,
            ]
        )

    def test_considers_a_four_of_a_kind_greater_than_another_by_comparing_a_card_in_both_four_of_a_kinds(self):
        other_cards = [
            Card(rank='2', suit='Clubs'),
            Card(rank='2', suit='Diamonds'),
            Card(rank='2', suit='Hearts'),
            Card(rank='2', suit='Spades')
        ]

        validator1 = FourOfAKindValidator(cards=self.cards)
        validator2 = FourOfAKindValidator(cards=other_cards)

        self.assertEqual(
            validator1 > validator2,
            True
        )