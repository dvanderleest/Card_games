"""
This is a dummy description for the Player module
"""

class Player():
    """
    Instances of this class have a name and a hand (list) of cards that can be used to play games. Individual cards can be any object, but are often an instance of thr Card class.
    """
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.hand = []

    def add_card_to_top_of_hand(self, card):
        """
        Add a card to the top of the hand
        """
        self.hand = card + self.hand

    def add_card_to_bottom_of_hand(self, card):
        """
        Add a card to the bottom of the hand
        """
        self.hand += card

    def play_card_at_position(self, card_index: int):
        """Returns the card at the given index and removes it from the players hand"""
        return self.hand.pop(card_index)

    def play_top_card(self):
        """Returns the card at top of the hand and removes it from the players hand"""
        return self.play_card_at_position(0)

    def play_bottom_card(self):
        """Returns the card at top of the hand and removes it from the players hand"""
        return self.play_card_at_position(-1)

    def get_current_hand(self):
        """Returns the current hand of cards"""
        return self.hand

    def sort_hand(self):
        """Sorts and sets the players current hand following lexicographical order"""
        self.hand = sorted(self.hand)
