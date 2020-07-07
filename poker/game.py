class Game():
    def __init__(self, deck, players):
        self.deck = deck
        self.players = players
        self.pot = 0
        self.folding_players = []
        self.tied_players = []

# This will be the bot's responsibility to invoke
    def play(self):
        self._shuffle_deck()
        self._deal_initial_two_cards_to_each_player()
        self._place_bets()

        self._deal_flop_cards()
        self._place_bets()

        self._deal_turn_card()
        self._place_bets()

        self._deal_river_card()
        self._place_bets()

        while len(self._winner()) > 1 and self._winner().count(max(self._winner())) == 1:
            self._deal_kicker_card()

        return self._winner()

    def _shuffle_deck(self):
        self.deck.shuffle()

    def _deal_initial_two_cards_to_each_player(self):
        for player in self.players:
            two_cards = self.deck.remove_cards(2)
            player.add_cards(two_cards)

    def _place_bets(self):
        for index, player in enumerate(self.players):
            if player.wants_to_fold():
                self.folding_players.append(self.players.pop(index))
            # add functionally for asking for bets (add to args bot and ctx for discord implementation)

    def _deal_community_cards(self, number_of_cards):
        flop_cards = self.deck.remove_cards(number_of_cards)
        for player in self.players:
            player.add_cards(flop_cards)

    def _deal_flop_cards(self):
        self._deal_community_cards(3)

    def _deal_turn_card(self):
        self._deal_community_cards(1)

    def _deal_river_card(self):
        self._deal_community_cards(1)

# ! add test suit
    def _winner(self):
        ranks = [
            player.hand.best_rank()[0]
            for player in self.players
        ]

        winning_rank = ranks.count(max(ranks))
        if winning_rank > 1:
            return [
                player.hand.cards
                for player in self.players
                if player.hand.best_rank()[0] == max(ranks)
            ]
        return [max(self.players)]

# ! add test suit
    def _deal_kicker_card(self):
        for player in self.players:
            kicker_card = self.deck.remove_cards(1)
            print(f'{player.name} was dealt {player.hand._cards}')
            player.hand.cards = kicker_card
