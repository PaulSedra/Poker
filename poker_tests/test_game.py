import unittest
from unittest.mock import MagicMock, call, patch

from poker.card import Card
from poker.game import Game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.first_two_cards = [
            Card(rank='2', suit='Hearts'),
            Card(rank='6', suit='Clubs')
        ]

        self.next_two_cards = [
            Card(rank='9', suit='Diamonds'),
            Card(rank='4', suit='Spades')
        ]

        self.flop_cards = [
            Card(rank='2', suit='Diamonds'),
            Card(rank='4', suit='Hearts'),
            Card(rank='10', suit='Spades')
        ]

        self.turn_card = [Card(rank='9', suit='Hearts')]

        self.river_card = [Card(rank='Queen', suit='Clubs')]

        self.mock_deck = MagicMock()
        self.mock_deck.remove_cards.side_effect = [
            self.first_two_cards,
            self.next_two_cards,
            self.flop_cards,
            self.turn_card,
            self.river_card
        ]

    def test_stores_deck_and_players(self):
        mock_deck = MagicMock()

        players = [
            MagicMock(),
            MagicMock()
        ]

        game = Game(
            deck = mock_deck,
            players = players
        )

        self.assertEqual(
            game.deck,
            mock_deck
        )

        self.assertEqual(
            game.players,
            players
        )

    @patch('poker.game.Game._winner')
    def test_game_play_shuffles_deck(self, mock_winner):
        mock_deck = MagicMock()

        players = [
            MagicMock(),
            MagicMock()
        ]

        game = Game(
            deck = mock_deck,
            players = players
        )

        game.play()

        mock_deck.shuffle.assert_called_once()

    @patch('poker.game.Game._winner')
    def test_deals_two_initial_cards_to_each_player(self, mock_winner):
        mock_player1 = MagicMock()
        mock_player2 = MagicMock()
        players = [mock_player1, mock_player2]

        game = Game(deck=self.mock_deck, players=players)

        game.play()

        self.mock_deck.remove_cards.assert_has_calls([
            call(2) for player in players
        ])

        mock_player1.add_cards.assert_has_calls([
            call(self.first_two_cards),
        ])
        mock_player2.add_cards.assert_has_calls([
            call(self.next_two_cards),
        ])

    @patch('poker.game.Game._winner')
    def test_pops_player_if_wants_to_fold_and_appends_to_folding_players_list(self, mock_winner):
        deck = MagicMock()
        player1 = MagicMock()
        player2 = MagicMock()

        player1.wants_to_fold.return_value = True
        player2.wants_to_fold.return_value = False
        players = [player1, player2]

        game = Game(deck=deck, players=players)
        game.play()

        self.assertEqual(
            game.folding_players,
            [player1]
        )

        self.assertEqual(
            game.players,
            [player2]
        )

    @patch('poker.game.Game._winner')
    def test_deals_three_flop_cards_one_turn_card_and_one_river_card_to_each_player(self, mock_winner):
        mock_player1 = MagicMock()
        mock_player1.wants_to_fold.return_value = False
        mock_player2 = MagicMock()
        mock_player2.wants_to_fold.return_value = False
        players = [mock_player1, mock_player2]


        game = Game(deck=self.mock_deck, players=players)
        game.play()

        self.mock_deck.remove_cards.assert_has_calls([
            call(3), call(1), call(1)
        ])

        calls = [
            call(self.flop_cards),
            call(self.turn_card),
            call(self.river_card)
        ]

        for player in players:
            player.add_cards.assert_has_calls(calls)