import guess
import constants

class Runner:
    def __init__(self, ciphertext):
        self.ct = ciphertext

    def main(self):
        Guess = guess(self.ct)