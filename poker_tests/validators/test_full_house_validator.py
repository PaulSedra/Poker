import unittest

from poker.card import Card
from poker.validators import FullHouseValidator

class FullHouseValidatorTest(unittest.TestCase):
    def setUp(self):
        self.three_of_clubs = Card(rank='3', suit='Clubs')
        self.three_of_hearts = Card(rank='3', suit='Hearts')
        self.three_of_spades = Card(rank='3', suit='Spades')
        self.nine_of_diamonds = Card(rank='9', suit='Diamonds')
        self.nine_of_spades = Card(rank='9', suit='Spades')

        self.cards = [
            self.three_of_clubs,
            self.three_of_hearts,
            self.three_of_spades,
            Card(rank='5', suit='Diamonds'),
            Card(rank='5', suit='Hearts'),
            self.nine_of_diamonds,
            self.nine_of_spades
        ]

    def test_validates_that_cards_have_a_pair_of_the_same_rank_and_three_of_another_rank(self):
        validator = FullHouseValidator(cards=self.cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_a_pair_of_cards_of_the_same_rank_and_three_of_another_rank_from_card_collection(self):
        validator = FullHouseValidator(cards=self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                self.three_of_clubs,
                self.three_of_hearts,
                self.three_of_spades,
                self.nine_of_diamonds,
                self.nine_of_spades
            ]
        )

    def test_considers_a_full_house_greater_than_another_by_comparing_a_card_in_both_three_of_a_kinds(self):
        other_cards = [
            Card(rank='2', suit='Diamonds'),
            Card(rank='2', suit='Diamonds'),
            Card(rank='2', suit='Diamonds'),
            Card(rank='Jack', suit='Diamonds'),
            Card(rank='Jack', suit='Diamonds')
        ]

        validator1 = FullHouseValidator(cards=self.cards)
        validator2 = FullHouseValidator(cards=other_cards)

        self.assertEqual(
            validator1 > validator2,
            True
        )

    def test_considers_a_full_house_greater_than_another_by_comparing_a_card_in_both_three_of_a_kinds_then_the_two_pairs(self):
        other_cards = [
            Card(rank='3', suit='Diamonds'),
            Card(rank='3', suit='Diamonds'),
            Card(rank='3', suit='Diamonds'),
            Card(rank='5', suit='Diamonds'),
            Card(rank='5', suit='Diamonds')
        ]

        validator1 = FullHouseValidator(cards=self.cards)
        validator2 = FullHouseValidator(cards=other_cards)

        self.assertEqual(
            validator1 > validator2,
            True
        )