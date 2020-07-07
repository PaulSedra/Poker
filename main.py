from poker.card import Card
from poker.deck import Deck
from poker.game import Game
from poker.hand import Hand
from poker.player import Player

deck = Deck()
cards = Card.create_standard_52_cards()
deck.add_cards(cards=cards)

hand1 = Hand()
hand2 = Hand()

player1 = Player(name='Paul', hand=hand1, bank=0)
player2 = Player(name='Boris', hand=hand2, bank=0)
players = [player1, player2]

game = Game(deck=deck, players=players)
winning_player = game.play()[0]

for player in players:
    print(f"{player.name} receives a {player.hand}.")
    index, best_hand_name, best_hand_cards = player.best_hand()
    hand_cards_strings = [str(card) for card in best_hand_cards]
    hand_cards_string = ' and '.join(hand_cards_strings)
    print(f"{player.name} has a {best_hand_name} with a {hand_cards_string}.")

print(f"The winner is {winning_player.name}.")


# from main import deck, cards, game, hand1, hand2, player1, player2


# TOFIX: there is a bug if the cards duplicate in the middle
# refer to class and test file

# TODO:
# Add __gt__ to all validators (with tests)
# https://www.adda52.com/poker/poker-rules/cash-game-rules/tie-breaker-rules

# refactor player __gt__
# add money
# add other things
# maybe add Kicker cards