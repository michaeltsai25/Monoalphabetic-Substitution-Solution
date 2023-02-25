import sys
sys.path.append("./Code/Env")
from guess import Guess
import unittest

class TestGuess(unittest.TestCase):

    def test_guess_reset(self):
        guess = Guess("abbcccddddeeeee")
        self.assertEqual(guess.guess, "edcba")
        self.assertEqual(guess.ct_to_pt, {'e':'e', 'd':'t', 'c':'a', 'b':'o', 'a':'i'})

    def test_decrypted(self):
        g = Guess("thisisatest")
        self.assertEqual(g.decrypted(), True)
        g = Guess("asdfghjkshouldbefalse")
        self.assertEqual(g.decrypted(), False)

    def test_num_words(self):
        g = Guess("thisgdhfyeiseuyatest")
        num = g.num_words()
        num = num[0]
        self.assertEqual(num, 4)

    def test_swap_general(self):
        g = Guess("test")
        self.assertEqual(g.swap_general(1), "tset")

if __name__ == "__main__":
    unittest.main()