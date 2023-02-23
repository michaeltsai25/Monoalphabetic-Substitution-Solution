import sys
sys.path.append("./Code/Env")
from utils import kl_divergence, calcFreq
from constants import DISTR_ENG_LETTERS

def analysis():
    """Stores a list of all of the kl-divergences in a text file."""
    samples = []
    kl_divs = []
    with open("/Users/michaeltsai/Documents/Github/Monoalphabetic-Substitution-Solution/TrainingData/TheHungerGames.txt", 'r') as new_file:
        samples = new_file.read().split("\n")
    for sample in samples:
        kl_divs.append(store_kl_divergence(sample))
    with open("/Users/michaeltsai/Documents/Github/Monoalphabetic-Substitution-Solution/Data/data.txt", 'w') as new_file:
        new_file.write(kl_divs)

def store_kl_divergence(sample):
    """Helper function for analysis."""
    freq = calcFreq(sample)
    freq = [freq[char] for char in freq]
    return kl_divergence(freq)