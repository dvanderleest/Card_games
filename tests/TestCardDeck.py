import random
import unittest
from src.card_deck import CardDeck

class TestCardDeckMethods(unittest.TestCase):

    def test_deck_shuffling_and_reset(self):
        fresh_deck = [
            (2, "clubs"), (3, "clubs"), (4, "clubs"), (5, "clubs"), 
            (6, "clubs"), (7, "clubs"), (8, "clubs"), (9, "clubs"), 
            (10, "clubs"), ("J", "clubs"), ("Q", "clubs"), ("K", "clubs"), ("A", "clubs"), 
            (2, "diamonds"), (3, "diamonds"), (4, "diamonds"), 
            (5, "diamonds"), (6, "diamonds"), (7, "diamonds"), 
            (8, "diamonds"), (9, "diamonds"), (10, "diamonds"), 
            ("J", "diamonds"), ("Q", "diamonds"), 
            ("K", "diamonds"), ("A", "diamonds"), 
            (2, "hearts"), (3, "hearts"), (4, "hearts"), (5, "hearts"), (6, "hearts"), (7, "hearts"), (8, "hearts"), (9, "hearts"), (10, "hearts"), ("J", "hearts"), ("Q", "hearts"), 
            ("K", "hearts"), ("A", "hearts"), 
            (2, "spades"), (3, "spades"), (4, "spades"), (5, "spades"), (6, "spades"), (7, "spades"), (8, "spades"), (9, "spades"), (10, "spades"), ("J", "spades"), ("Q", "spades"), 
            ("K", "spades"), ("A", "spades")
        ]
        
        # Generate an instance of the CardDeck class
        my_deck = CardDeck()

        # Check that the instance is correctly initialized
        self.assertEqual(my_deck.current, fresh_deck)
        
        
        #Set a fixed seed and shuffle the deck
        seed = 0xBEEF
        random.seed(seed)
        my_deck.shuffle()
        expected_shuffled_deck = [
            (4, "diamonds"), ("Q", "hearts"), (8, "spades"), 
            (5, "clubs"), ("A", "spades"), (3, "clubs"), (2, "spades"), (7, "spades"), (6, "hearts"), 
            (2, "diamonds"), (10, "spades"), (8, "clubs"), (3, "spades"), ("K", "hearts"), (3, "diamonds"), ("J", "clubs"), 
            ("K", "diamonds"), (8, "diamonds"), (5, "spades"), 
            ("J", "diamonds"), ("J", "hearts"), (2, "hearts"), 
            (4, "hearts"), (6, "diamonds"), ("A", "clubs"), (6, "clubs"), ("K", "spades"), (5, "diamonds"), ("A", "hearts"), 
            ("J", "spades"), ("K", "clubs"), (9, "hearts"), (2, "clubs"), ("Q", "clubs"), (3, "hearts"), (10, "diamonds"), 
            ("Q", "spades"), (9, "spades"), (9, "diamonds"), 
            (7, "hearts"), (5, "hearts"), ("A", "diamonds"), 
            (9, "clubs"), ("Q", "diamonds"), (6, "spades"), 
            (10, "hearts"), (7, "diamonds"), (10, "clubs"), (7, "clubs"), (4, "spades"), (8, "hearts"), (4, "clubs")
        ]

        self.assertEqual(my_deck.current, expected_shuffled_deck)

        # Check that resetting the instance results in a fresh deck
        my_deck.reset()
        self.assertEqual(my_deck.current, fresh_deck)

if __name__ == '__main__':
    unittest.main()
