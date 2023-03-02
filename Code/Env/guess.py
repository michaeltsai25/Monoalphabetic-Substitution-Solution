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
        for key in desc_order.keys():
            chars.append(key)
        guess_desc_order = [freq_list[i] for i in range(len(desc_order))]
        for i in range(len(chars)):
            self.ct_to_pt[chars[i]] = guess_desc_order[i]
        for char in self.ciph_text:
            self.guess += self.ct_to_pt[char]

    def decrypted(self, test=False):
        """Checks to see if the guess is decrypted"""
        if test == True:
            g = self.ciph_text
        else:
            g = self.guess
        count, g = self.num_words()
        if len(g) == 0:
            return True
        return False
    
    #Spurious key occurs, possibly rewrite this method
    def num_words(self, test=False):
        """Counts the number of words decrypted in the guess"""
        if test == True:
            g = self.ciph_text
        else:
            g = self.guess
        count = 0
        with open('dictionary.txt', 'r') as new_file:
            file = new_file.read()
            word_list = file.split("\n")
            for word in word_list:
                if word in g: #self.guess:
                    print(g)
                    print(word)
                    g = g.replace(word, "")
                    count += 1
        return count, g

    def random_swap_neigh_chars(self):
       ct_list = self.ct_to_pt.keys()
       pt_list = self.ct_to_pt.values()
       x = randint(0, len(ct_list))
       self.swap_general(ct_list, pt_list, x)

    def swap_general(self, ct_list, pt_list, x):
        """Swaps two neighboring letters"""
        char = ct_list[x]
        ct_list[x] = ct_list[x+1]
        ct_list[x+1] = char
        for i in range(len(ct_list)):
            self.ct_to_pt[ct_list[i]] = pt_list[i]

if __name__ == "__main__":
    g = Guess("thisisatest")
    print(g.num_words(test=True))