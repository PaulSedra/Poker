import unittest

from poker.card import Card
from poker.validators import RoyalFlushValidator

class RoyalFlushValidatorTest(unittest.TestCase):
    def test_validates_that_cards_do_not_have_five_consecutive_cards_of_the_same_suit_ending_in_ace(self):
        cards = [
            Card(rank='9', suit='Clubs'),
            Card(rank='10', suit='Clubs'),
            Card(rank='Jack', suit='Clubs'),
            Card(rank='Queen', suit='Clubs'),
            Card(rank='King', suit='Clubs'),
            Card(rank='Ace', suit='Diamonds')
        ]

        validator = RoyalFlushValidator(cards=cards)

        self.assertEqual(
            validator.is_valid(),
            False
        )

    def test_validates_that_cards_have_five_consecutive_cards_of_the_same_suit_ending_in_ace(self):
        cards = [
            Card(rank='9', suit='Clubs'),
            Card(rank='10', suit='Clubs'),
            Card(rank='Jack', suit='Clubs'),
            Card(rank='Queen', suit='Clubs'),
            Card(rank='King', suit='Clubs'),
            Card(rank='Ace', suit='Clubs'),
            Card(rank='Ace', suit='Diamonds'),
        ]

        validator = RoyalFlushValidator(cards=cards)

        self.assertEqual(
            validator.is_valid(),
            True
        )

    def test_returns_five_consecutive_cards_of_the_same_suit_ending_in_ace_from_card_collection(self):
        ten_of_clubs = Card(rank='10', suit='Clubs')
        jack_of_clubs = Card(rank='Jack', suit='Clubs')
        queen_of_clubs = Card(rank='Queen', suit='Clubs')
        king_of_clubs = Card(rank='King', suit='Clubs')
        ace_of_clubs = Card(rank='Ace', suit='Clubs')
        
        cards = [
            Card(rank='9', suit='Clubs'),
            ten_of_clubs,
            jack_of_clubs,
            queen_of_clubs,
            king_of_clubs,
            ace_of_clubs,
            Card(rank='Ace', suit='Diamonds')
        ]

        validator = RoyalFlushValidator(cards=cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                ten_of_clubs,
                jack_of_clubs,
                queen_of_clubs,
                king_of_clubs,
                ace_of_clubs
            ]
        )