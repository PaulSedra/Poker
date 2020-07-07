import unittest
from poker.card import Card

class CardTest(unittest.TestCase):
    def test_card_object_attributes(self):
        card = Card(rank='Queen', suit='Hearts')
        self.assertEqual(card.rank, 'Queen')
        self.assertEqual(card.suit, 'Hearts')

    def test_knows_its_rank_index(self):
        card = Card(rank='Jack', suit='Hearts')
        self.assertEqual(card.rank_index, 9)

    def test_has_string_representation(self):
        card = Card('5', 'Diamonds')
        self.assertEqual(str(card), '5 of Diamonds')

    def test_has_technical_representation(self):
        card = Card('5', 'Diamonds')
        self.assertEqual(repr(card), "Card('5', 'Diamonds')")

    def test_card_has_four_possible_suit_options(self):
        self.assertEqual(
            Card.SUITS,
            ('Hearts', 'Clubs', 'Spades', 'Diamonds')
        )
    
    def test_card_has_thirteen_possible_rank_options(self):
        self.assertEqual(
            Card.RANKS,
            (
                '2', '3', '4', '5', '6', '7', '8', '9', '10',
                'Jack', 'Queen', 'King', 'Ace'
            )
        )

    def test_card_only_allows_for_valid_rank(self):
        with self.assertRaises(ValueError):
            Card(rank='Two', suit='Hearts')
    
    def test_card_only_allows_for_valid_suit(self):
        with self.assertRaises(ValueError):
            Card(rank='2', suit='Dots')

    def test_can_create_standard_52_cards(self):
        cards = Card.create_standard_52_cards()
        self.assertEqual(len(cards), 52)
        self.assertEqual(
            cards[0],
            Card(rank='2', suit='Hearts')
        )
        
        self.assertEqual(
            cards[-1],
            Card(rank='Ace', suit='Diamonds')
        )

    def test_considers_cards_equal_if_they_have_the_same_rank_and_suit(self):
        self.assertEqual(
            Card(rank='2', suit='Hearts'),
            Card(rank='2', suit='Hearts')
        )

    def test_card_can_sort_itself_with_another_one(self):
        queen_of_spades = Card(rank='Queen', suit='Spades')
        king_of_spades = Card(rank='King', suit='Spades')
        self.assertTrue(
            queen_of_spades < king_of_spades,
            'Card can evaluate itself with another one'
        )

    def test_sorts_cards_by_rank_then_suit(self):
        two_of_spades = Card(rank='2', suit='Spades')
        five_of_diamonds = Card(rank='5', suit='Diamonds')
        five_of_hearts = Card(rank='5', suit='Hearts')
        eight_of_hearts = Card(rank='8', suit='Hearts')
        ace_of_clubs = Card(rank='Ace', suit='Clubs')

        unsorted_cards = [
            five_of_hearts,
            two_of_spades,
            five_of_diamonds,
            ace_of_clubs,
            eight_of_hearts
        ]

        unsorted_cards.sort(),

        self.assertEqual(
            unsorted_cards,
            [
                two_of_spades,
                five_of_diamonds,
                five_of_hearts,
                eight_of_hearts,
                ace_of_clubs
            ]
        )