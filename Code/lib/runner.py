import sys
sys.path.append("./Code/lib")
from guess import Guess
from constants import *
from utils import *

class Runner:
    def __init__(self, ciphertext):
        self.ct = ciphertext

    def main(self):
        guess = Guess(self.ct)
        count = 0
        c = 0
        last  = ""
        while not guess.decrypted() or guess.guess == "wheniwakeuptheothersideofthebediscoldmyfingersstretchoutseekingprimswarmthbutfindingonlytheroughcanvascoverofthemattressshemusthavehadbaddreamsandclimbedinwithourmotherofcourseshedidthisisthedayofthereapingmylittlesisterprimcurleduponhersidecocoonedinmymothersbodytheircheekspressedtogetherinsleepmymotherlooksyoungerstillwornbutnotsobeatendown":
            n = guess.num_words()
            x = guess.random_swap_neigh_chars()
            freq = [value for value in calcFreq(guess.guess).values()]
            if guess.num_words() < n or kl_divergence(freq) > MAX_KL_DIV:
                guess.swap_general(x)
            if count > MAX_ITER and guess.num_words() < MIN_WORDS:
                guess.reset()
            #count += 1 #count doesn't work, have to adjust logic
            c += 1
            if c >= 100:
                break
            if not guess.guess == last:
                print(guess.guess) #just to track the evolution of the algorithm's guesses, may remove if desired
                print(guess.ct_to_pt)
                last = guess.guess
        return guess.guess

if __name__ == "__main__":
    r = Runner("jkaszjrnacfpkalpkayqzxalbpkadaxzqtlixgebzswayqqpyaptklcpqaanzswfyzgqjrygpkdcpbzsxzswlsiepkaylcwktrshrqtlhaylbpkagrppyaqqqkagcqpkrhakrxdrxxyargqrsxtizgdaxzsjzpklcyglpkaylbtlcyqaqkaxzxpkzqzqpkaxrelbpkayarfzswgeizppiaqzqpayfyzgtcyiaxcflskayqzxatltllsaxzsgeglpkayqdlxepkazytkaanqfyaqqaxplwapkayzsqiaafgeglpkayillnqelcswayqpziijlysdcpslpqldarpasxljs")
    r.main()