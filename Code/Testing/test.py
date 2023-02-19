import timeit
import sys
sys.path.append("/Users/michaeltsai/Documents/GitHub/Monoalphabetic-Substitution-Solution/./Code/Env")
from guess import Guess

def test_guess_reset():
    pass

def test_generate_data():
    pass

def time_num_words():
    """Just a function to test the runtime of looping through dictionary"""
    g = Guess("thisisatesttoseetheruntimeofthefunctionnumwords")
    print(g.num_words())

if __name__ == "__main__":
    time_num_words()