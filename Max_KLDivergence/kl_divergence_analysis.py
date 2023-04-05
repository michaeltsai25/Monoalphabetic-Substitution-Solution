import sys
sys.path.append("./Code/lib")
from utils import calcFreq, read_data
from constants import DISTR_ENG_LETTERS
from statistics import mean
from scipy.special import kl_div

def analysis():
    """Stores a list of all of the kl-divergences in a text file."""
    samples = []
    kl_divs = []
    with open("/Users/michaeltsai/Documents/Github/Monoalphabetic-Substitution-Solution/TrainingData/TheHungerGames.txt", 'r') as new_file:
        samples = new_file.read().split("\n")
    for sample in samples:
        kl_divs.append(store_kl_divergence(sample))
    with open("/Users/michaeltsai/Documents/Github/Monoalphabetic-Substitution-Solution/Data/Distr_data.txt", 'w') as new_file:
        new_file.write(str(kl_divs))

def store_kl_divergence(sample):
    """Helper function for analysis."""
    freq = calcFreq(sample)
    freq = list(freq.values())
    return round(kl_div(freq), 2)

def sampling_distr():
    data = read_data("Distr_data.txt")
    samp_means = []
    x = 0
    for i in range(len(data)):
        if i%50 == 0 and i != 0:
            samp_means.append(round(mean(data[x:i]), 2))
            x = i
    with open("/Users/michaeltsai/Documents/Github/Monoalphabetic-Substitution-Solution/Data/Samp_Distr.txt", 'w') as new_file:
        new_file.write(str(samp_means))

if __name__ == "__main__":
    sampling_distr()