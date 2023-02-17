import utils
from random import randint

class Guess:
    def __init__(self, ciphertext):
        self.ciph_text = ciphertext.replace(" ", "")
        self.guess = ""
        self.ct_to_pt = {}
        self.reset()

    def reset(self):
        """Initializes the guess based on frequencies, modifies ct_to_pt as necessary"""
        freq_list = "etaoinshrdlcumwfgypbvkjxqz"
        desc_order = utils.calcFreq(self.ciph_text)
        chars = []
        for key, item in desc_order:
            chars.append(key)
        guess_desc_order = [freq_list[i] for i in range(len(desc_order))]
        for i in range(len(chars)):
            self.ct_to_pt[chars[i]] = guess_desc_order[i]
        for char in self.ciph_text:
            self.guess += self.ct_to_pt[char]

    def decrypted(self):
        """Checks to see if the guess is decrypted"""
        count, g = self.num_words()
        if len(g) == 0:
            return True
        return False
    
    def num_words(self):
        """Counts the number of words decrypted in the guess"""
        g = self.guess
        count = 0
        with open('dictionary.txt', 'r') as new_file:
            word_list = new_file.split("\n")
            for word in word_list: #check to see if this creates runtime issues
                if word in self.guess:
                    g.replace(word, "")
                    count += 1
        return count, g

    def random_swap_neigh_chars(self):
        """Randomly swaps neighboring letters in the guess"""
        x = randint(0, len(self.guess)-1)
        self.swap_general(x)
        return x

    def swap_general(self, x):
        """Swaps two neighboring letters"""
        g = self.Convert(self.guess)
        char = g[x]
        g[x] = g[x+1]
        g[x+1] = char
        self.guess = "".join(g)

    def Convert(self, string):
        """Helper function for random_swap_neigh_chars, converts a string to a list of chars"""
        list1 = []
        list1[:0] = string
        return list1