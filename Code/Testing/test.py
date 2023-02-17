from Env import guess
from . import Generate_Data
import timeit

def test_guess_reset():
    pass

def test_generate_data():
    pass

def time_num_words():
    """Just a function to test the runtime of looping through dictionary"""
    g = guess.Guess("thisisatesttoseetheruntimeofthefunctionnumwords")
    print(g.num_words())