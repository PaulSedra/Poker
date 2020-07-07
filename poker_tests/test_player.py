import unittest
from unittest.mock import MagicMock

from poker.card import Card
from poker.hand import Hand
from poker.player import Player
from poker.validators import PairValidator

class PlayerTest(unittest.TestCase):
    def test_stores_name_and_cards(self):
        hand = Hand()
        player = Player(name='Boris', hand=hand, bank=0)
        self.assertEqual(player.name, 'Boris')
        self.assertEqual(player.hand, hand)

    def test_figures_out_own_best_hand(self):
        mock_hand = MagicMock()
        mock_hand.best_rank.return_value = 'Straight Flush'

        player = Player(name='Boris', hand=mock_hand, bank=0)

        self.assertEqual(
            player.best_hand(),
            'Straight Flush'
        )

        mock_hand.best_rank.assert_called()

    def test_passes_new_cards_to_hand(self):
        mock_hand = MagicMock()
        player = Player(name='Boris', hand=mock_hand, bank=0)

        cards = [
            Card(rank='Ace', suit='Spades'),
            Card(rank='Queen', suit='Diamonds')
        ]

        player.add_cards(cards)

        mock_hand.add_cards.assert_called_with(cards)

    def test_decides_to_continue_or_drop_out_of_game(self):
        player = Player(name='Sharon', hand=Hand(), bank=0)
        self.assertEqual(
            player.wants_to_fold(),
            False
        )

    def test_sorts_players_by_best_hand(self):
        mock_hand1 = MagicMock()
        mock_hand1.best_rank.return_value = (2, 'Four of a Kind', [])
        mock_hand2 = MagicMock()
        mock_hand2.best_rank.return_value = (0, 'Royal Flush', [])

        player1 = Player(name='Kimberly', hand=mock_hand1, bank=0)
        player2 = Player(name='Debbie', hand=mock_hand2, bank=0)

        players = [player1, player2]

        self.assertEqual(
            max(players),
            player2
        )

    def test_sorts_players_by_hand_value_if_players_tie(self):
        cards1 = [Card(rank='4', suit='Hearts'), Card(rank='4', suit='Diamonds')]
        hand1 = Hand()
        hand1.add_cards(cards1)

        cards2 = [Card(rank='2', suit='Hearts'), Card(rank='2', suit='Diamonds')]
        hand2 = Hand()
        hand2.add_cards(cards2)

        player1 = Player(name='Kimberly', hand=hand1, bank=0)
        player2 = Player(name='Debbie', hand=hand2, bank=0)

        players = [player1, player2]

        self.assertEqual(
            max(players).name,
            player1.name
        )