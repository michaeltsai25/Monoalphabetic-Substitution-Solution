from guess import Guess
import constants

class Runner:
    def __init__(self, ciphertext):
        self.ct = ciphertext

    def main(self):
        guess = Guess(self.ct)