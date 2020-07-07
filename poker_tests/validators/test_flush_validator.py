import unittest

from poker.card import Card
from poker.validators import FlushValidator

class FlushValidatorTest(unittest.TestCase):
    def setUp(self):
        self.five_of_hearts = Card(rank='5', suit='Hearts')
        self.seven_of_hearts = Card(rank='7', suit='Hearts')
        self.eight_of_hearts = Card(rank='8', suit='Hearts')
        self.ten_of_hearts = Card(rank='10', suit='Hearts')
        self.ace_of_hearts = Card(rank='Ace', suit='Hearts')

        self.cards = [
            Card(rank='2', suit='Hearts'),
            self.five_of_hearts,
            self.seven_of_hearts,
            self.eight_of_hearts,
            self.ten_of_hearts,
            Card(rank='Jack', suit='Clubs'),
            self.ace_of_hearts
        ]

    def test_validates_that_cards_have_five_of_the_same_suit(self):
        validator = FlushValidator(cards=self.cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_the_five_highest_cards_of_the_same_suit_from_card_collection(self):
        validator = FlushValidator(cards=self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
            self.five_of_hearts,
            self.seven_of_hearts,
            self.eight_of_hearts,
            self.ten_of_hearts,
            self.ace_of_hearts
            ]
        )

    def test_considers_a_flush_greater_than_another_by_comparing_the_highest_card_in_both_flushes(self):
        other_cards = [
            Card(rank='5', suit='Diamonds'),
            Card(rank='7', suit='Diamonds'),
            Card(rank='9', suit='Diamonds'),
            Card(rank='10', suit='Diamonds'),
            Card(rank='Jack', suit='Diamonds')
        ]

        validator1 = FlushValidator(cards=self.cards)
        validator2 = FlushValidator(cards=other_cards)

        self.assertEqual(
            validator1 > validator2,
            True
        )