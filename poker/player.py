class Player():
    def __init__(self, name, hand, bank):
        self.name = name
        self.hand = hand
        self.bank = bank

    def __eq__(self, other_player):
        validators = self._validators(other_player)
        return validators[0] == validators[1]

    def __gt__(self, other_player):
        validators = self._validators(other_player)
        if self.best_hand()[0] == other_player.best_hand()[0]:
            return validators[0] == max(validators)
        return self.best_hand()[0] < other_player.best_hand()[0]

    def _validators(self, other_player):
        self.hand.best_rank()
        other_player.hand.best_rank()
        return [
            self.hand._validator(cards=self.hand.cards),
            other_player.hand._validator(cards=other_player.hand.cards)
        ]

    def best_hand(self):
        return self.hand.best_rank()

    def add_cards(self, cards):
        self.hand.add_cards(cards)

    def wants_to_fold(self):
        # add implementation for askinf user if they want to fold (add args bot and ctx for discord implementation)
        return False