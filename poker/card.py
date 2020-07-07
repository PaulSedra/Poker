class Card():
    SUITS = ('Hearts', 'Clubs', 'Spades', 'Diamonds')

    RANKS = (
                '2', '3', '4', '5', '6', '7', '8', '9', '10',
                'Jack', 'Queen', 'King', 'Ace'
            )

    @classmethod
    def create_standard_52_cards(cls):
        return [
            cls(rank=rank, suit=suit)
            for suit in cls.SUITS
            for rank in cls.RANKS
        ]

    def __init__(self, rank, suit):
        if rank not in self.RANKS:
            raise ValueError(f"Invalid rank. Rank must be one of the following: {self.RANKS}")

        if suit not in self.SUITS:
            raise ValueError(f"Invalid suit. Suit must be one of the following: {self.RANKS}")

        self.rank = rank
        self.rank_index = self.RANKS.index(rank)
        self.suit = suit

    def __str__(self):
        return f'{self.rank} of {self.suit}'

    def __repr__(self):
        return f"Card('{self.rank}', '{self.suit}')"

    def __eq__(self, other_card):
        return self.rank == other_card.rank and self.suit == other_card.suit
    
    def __gt__(self, other_card):
        if self.rank == other_card.rank:
            return self.suit > other_card.suit

        return self.rank_index > other_card.rank_index