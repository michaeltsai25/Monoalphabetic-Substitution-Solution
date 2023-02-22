import sys
sys.path.append("./Code/Env")
from guess import Guess
import unittest

class TestGuess(unittest.TestCase):
    def test_guess_reset(self):
        pass

    def test_generate_data(self):
        pass

    def time_num_words(self):
        g = Guess("thisisatesttoseetheruntimeofthefunctionnumwords")
        num = g.num_words()
        self.assertEqual(num[0], 14)

if __name__ == "__main__":
    unittest.main()