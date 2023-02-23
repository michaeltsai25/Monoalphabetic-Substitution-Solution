from math import log
from scipy.special import rel_entr
from constants import DISTR_ENG_LETTERS
import os

def kl_divergence(cipherDistr):
    """Calculates the KL-Divergence from the input distribution to the distribution of letters in the English language"""
    return sum(rel_entr(cipherDistr, DISTR_ENG_LETTERS[0:len(cipherDistr)]))

def calcFreq(ciphText):
    """Orders the characters in the text from least common to most common"""
    freq = store_freq(ciphText)
    return dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))

def store_freq(ciphText):
    """Helper function for calcFreq"""
    text = "".join(set(ciphText))
    freq = {}
    for char in text:
        freq[char] = ciphText.count(char)/len(ciphText)
    return freq

def read_data(name):
    with open(os.path.join("/Users/michaeltsai/Documents/Github/Monoalphabetic-Substitution-Solution/Data/", name), 'r') as new_file:
        data = new_file.read()
        data = data.replace('[', "")
        data = data.replace(']', "")
        data = data.split(", ")
        data = [float(point) for point in data]
    return data

if __name__ == "__main__":
    print(kl_divergence([0.5, 0.5], [0.25, 0.25]))