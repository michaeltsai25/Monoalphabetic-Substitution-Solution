from guess import Guess
from constants import MAX_KL_DIV
from utils import kl_divergence

class Runner:
    #is a class necessary here?
    def __init__(self, ciphertext):
        self.ct = ciphertext

    def main(self):
        guess = Guess(self.ct)
        num_words = 0
        while not guess.decrypted():
            x = guess.random_swap_neigh_chars()
            count, g = guess.num_words()
            if count < num_words: #also add the business about the kl divergence
                guess.swap_general(x)
            num_words = count
        return guess.guess