from math import log
from scipy.special import rel_entr
from constants import DISTR_ENG_LETTERS

def kl_divergence(cipherDistr):
    """Calculates the KL-Divergence from the input distribution to the distribution of letters in the English language"""
    return sum(rel_entr(cipherDistr, DISTR_ENG_LETTERS[0:len(cipherDistr)]))

def calcFreq(ciphText):
    """Orders the characters in the text from least common to most common"""
    freq = store_freq(ciphText)
    return sorted(freq.items(), key=lambda x: x[1])

def store_freq(ciphText):
    """Helper function for calcFreq"""
    text = "".join(set(ciphText))
    freq = {}
    for char in text: 
        freq[char] = ciphText.count(char)/len(ciphText)
    return freq

if __name__ == "__main__":
    print(kl_divergence([0.5, 0.5], [0.25, 0.25]))