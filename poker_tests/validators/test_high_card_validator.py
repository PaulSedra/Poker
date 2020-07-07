import unittest

from poker.card import Card
from poker.validators import HighCardValidator

class HighCardValidatorTest(unittest.TestCase):
    def test_validates_that_cards_have_a_high_card(self):
        cards = [
            Card(rank='7', suit='Clubs'),
            Card(rank='Ace', suit='Diamonds')
        ]

        validator = HighCardValidator(cards=cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_high_card_from_card_collection(self):
        ace_of_diamonds = Card(rank='Ace', suit='Diamonds')

        cards = [
            Card(rank='5', suit='Spades'),
            Card(rank='8', suit='Diamonds'),
            Card(rank='10', suit='Clubs'),
            Card(rank='Queen', suit='Spades'),
            ace_of_diamonds
        ]

        validator = HighCardValidator(cards=cards)

        self.assertEqual(
            validator.valid_cards(),
            [ace_of_diamonds]
        )

    def test_considers_a_high_card_greater_than_another_by_comparing_the_cards_by_their_index(self):
        cards1 = [
            Card(rank='7', suit='Clubs'),
            Card(rank='Ace', suit='Diamonds')
        ]
        cards2 = [
            Card(rank='7', suit='Clubs'),
            Card(rank='Jack', suit='Diamonds')
        ]

        validator1 = HighCardValidator(cards=cards1)
        validator2 = HighCardValidator(cards=cards2)

        self.assertEqual(
            validator1 > validator2,
            True
        )