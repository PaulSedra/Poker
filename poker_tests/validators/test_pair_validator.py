import unittest

from poker.card import Card
from poker.validators import PairValidator

class PairValidatorTest(unittest.TestCase):
    def setUp(self):
        self.ten_of_clubs = Card(rank='10', suit='Clubs')
        self.ten_of_spades = Card(rank='10', suit='Spades')

        self.cards = [
            Card(rank='3', suit='Hearts'),
            Card(rank='5', suit='Diamonds'),
            self.ten_of_clubs,
            self.ten_of_spades,
            Card(rank='King', suit='Clubs')
        ]

    def test_validates_that_cards_have_exactly_one_pair(self):
        cards = [
            Card(rank='Ace', suit='Spades'),
            Card(rank='Ace', suit='Clubs')
        ]

        validator = PairValidator(cards=cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_pair_from_card_collection(self):
        validator = PairValidator(cards=self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [self.ten_of_clubs, self.ten_of_spades]
        )

    def test_considers_a_pair_greater_than_another_by_comparing_a_card_in_both_pairs(self):
        other_cards = [
            Card(rank='3', suit='Hearts'),
            Card(rank='5', suit='Diamonds'),
            Card(rank='8', suit='Clubs'),
            Card(rank='8', suit='Diamonds'),
            Card(rank='King', suit='Clubs')
        ]

        validator1 = PairValidator(cards=self.cards)
        validator2 = PairValidator(cards=other_cards)

        self.assertEqual(
            validator1 > validator2,
            True
        )