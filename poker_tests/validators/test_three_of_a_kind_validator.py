import unittest

from poker.card import Card
from poker.validators import ThreeOfAKindValidator

class ThreeOfAKindValidatorTest(unittest.TestCase):
    def setUp(self):
        self.king_of_clubs = Card(rank='King', suit='Clubs')
        self.king_of_diamonds = Card(rank='King', suit='Diamonds')
        self.king_of_hearts = Card(rank='King', suit='Hearts')

        self.cards = [
            Card(rank='5', suit='Clubs'),
            self.king_of_clubs,
            self.king_of_diamonds,
            self.king_of_hearts,
            Card(rank='Ace', suit='Spades')
        ]

    def test_validates_that_cards_have_exactly_three_of_the_same_rank(self):
        validator = ThreeOfAKindValidator(cards=self.cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_three_of_a_kind_from_card_collection(self):
        validator = ThreeOfAKindValidator(cards=self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                self.king_of_clubs,
                self.king_of_diamonds,
                self.king_of_hearts
            ]
        )

    def test_considers_a_three_of_a_kind_greater_than_another_by_comparing_a_card_in_both_three_of_a_kinds(self):
        other_cards = [
            Card(rank='5', suit='Clubs'),
            Card(rank='9', suit='Clubs'),
            Card(rank='9', suit='Diamonds'),
            Card(rank='9', suit='Hearts'),
            Card(rank='Ace', suit='Spades')
        ]

        validator1 = ThreeOfAKindValidator(cards=self.cards)
        validator2 = ThreeOfAKindValidator(cards=other_cards)

        self.assertEqual(
            validator1 > validator2,
            True
        )