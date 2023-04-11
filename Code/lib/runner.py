import sys
sys.path.append("./Code/lib")
from guess import Guess
from constants import *
from utils import *

class Runner:
    #is a class necessary here?
    def __init__(self, ciphertext):
        self.ct = ciphertext

    def main(self):
        guess = Guess(self.ct)
        while not guess.decrypted() or guess.guess == "wheniwakeuptheothersideofthebediscold":
            count = 0
            n = guess.num_words()
            x = guess.random_swap_neigh_chars()
            freq = [value for value in calcFreq(guess.guess).values()]
            if guess.num_words() < n or kl_divergence(freq) > MAX_KL_DIV:
                guess.swap_general(x)
            if count > MAX_ITER and guess.num_words() < MIN_WORDS:
                guess.reset()
            count += 1
            #print(guess.guess) #just to track the evolution of the algorithm's guesses, may remove if desired
        return guess.guess

if __name__ == "__main__":
    r = Runner("mteormiqeslntegntevjrwegunteaewrjcgxw")
    r.main()