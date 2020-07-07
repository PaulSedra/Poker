import unittest

from poker.card import Card
from poker.validators import TwoPairValidator

class TwoPairValidatorTest(unittest.TestCase):
    def setUp(self):
        self.king_of_diamonds = Card(rank='King', suit='Diamonds')
        self.king_of_hearts = Card(rank='King', suit='Hearts')
        self.ace_of_clubs = Card(rank='Ace', suit='Clubs')
        self.ace_of_spades = Card(rank='Ace', suit='Spades')

        self.cards = [
            Card(rank='5', suit='Clubs'),
            self.king_of_diamonds,
            self.king_of_hearts,
            self.ace_of_clubs,
            self.ace_of_spades
        ]

    def test_validates_that_cards_have_at_least_two_pairs(self):
        validator = TwoPairValidator(cards=self.cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_pairs_from_card_collection(self):
        validator = TwoPairValidator(cards=self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                self.king_of_diamonds,
                self.king_of_hearts,
                self.ace_of_clubs,
                self.ace_of_spades
            ]
        )

    def test_considers_a_two_pair_greater_than_another_by_comparing_a_card_of_the_highest_pair_in_both_two_pairs(self):
        other_cards = [
            Card(rank='Queen', suit='Diamonds'),
            Card(rank='Queen', suit='Hearts'),
            Card(rank='King', suit='Clubs'),
            Card(rank='King', suit='Spades')
        ]

        validator1 = TwoPairValidator(cards=self.cards)
        validator2 = TwoPairValidator(cards=other_cards)

        self.assertEqual(
            validator1 > validator2,
            True
        )

    def test_considers_a_two_pair_greater_than_another_by_comparing_a_card_of_the_highest_pair_in_both_two_pairs_then_the_other_pairs(self):
        other_cards = [
            Card(rank='Jack', suit='Diamonds'),
            Card(rank='Jack', suit='Hearts'),
            Card(rank='Ace', suit='Clubs'),
            Card(rank='Ace', suit='Spades')
        ]

        validator1 = TwoPairValidator(cards=self.cards)
        validator2 = TwoPairValidator(cards=other_cards)

        self.assertEqual(
            validator1 > validator2,
            True
        )