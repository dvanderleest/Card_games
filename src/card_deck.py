"""
Module holding card and deck logic including card creating and shuffling
"""
import random

class CardDeck():
    """Class that acts as a digital twin of physical cards."""

    VALUES = list(v for v in list(range(2,11)) + ["J", "Q", "K", "A"])

    SUITS = {"clubs": "♣",
            "diamonds": "♦",
            "hearts": "♥",
            "spades": "♠"}

    def __init__(self) -> None:
        """Creating a deck of cards"""
        self.current = []
        self.reset()

    def show(self, pretty=False) -> None:
        """Print current deck and bounce"""
        if not pretty:
            print(self.current)
        else:
            curr = []
            for card in self.current:
                curr.append((card[0], CardDeck.SUITS[card[1]]))
            print(curr)

    def reset(self) -> None:
        """Set the current deck of the deck object to the ordered default"""
        self.current = list((v, s) for s in CardDeck.SUITS for v in CardDeck.VALUES)

    def shuffle(self) -> None:
        """"Shuffle the current deck"""
        random.shuffle(self.current)

    def deal_n_cards(self, n) -> list:
        """"Get a given number (n) cards from the current deck of cards"""

        cards = []
        for _ in range(n):
            cards.append(self.current.pop())

        return cards
