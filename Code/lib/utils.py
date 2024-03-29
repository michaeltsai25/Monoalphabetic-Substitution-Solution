import os
from constants import DISTR_ENG_LETTERS, ALPH, DISTR_ENG_LETTERS_ALPH
from scipy.special import rel_entr
import numpy as np

def calc_bigram_freq(ciphText):
    np.set_printoptions(linewidth=375)
    freq_table=np.zeros(shape=(26,26))
    for i in range(len(ciphText)-1):
        freq_table[ALPH.index(ciphText[i+1]),ALPH.index(ciphText[i])] += 1
    return freq_table/(len(ciphText)-1)

def calcFreq2(ciphText):
    freq=[]
    for char in ALPH:
        freq.append(ciphText.count(char)/(len(ciphText)))
    return freq

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
    #with open(os.path.join("/Users/michaeltsai/Documents/Github/Monoalphabetic-Substitution-Solution/Data/", name), 'r') as new_file:
    with open(os.path.join("Data/", name), 'r') as new_file:
        data = new_file.read()
        data = data.replace('[', "")
        data = data.replace(']', "")
        data = data.split(", ")
        data = [float(point) for point in data]
    return data

def read_dictionary():
    return read_file("dictionary.txt")

def read_plaintext():
    return read_file("Data/TrainingData/TheHungerGames.txt")

def read_file(file):
    """Helper function for read_dictionary and read_plaintext"""
    with open(file, 'r') as new_file:
        dic = new_file.read()
        dic = dic.split('\n')
    return dic

def kl_divergence(cipherDistr, alph_order=False):
    """Calculates the KL-Divergence from the input distribution to the distribution of letters in the English language"""
    if alph_order:
        return sum(rel_entr(cipherDistr, DISTR_ENG_LETTERS_ALPH[0:len(cipherDistr)]))
    return sum(rel_entr(cipherDistr, DISTR_ENG_LETTERS[0:len(cipherDistr)]))

if __name__ == "__main__":
    print(calc_bigram_freq("thisisatest"))