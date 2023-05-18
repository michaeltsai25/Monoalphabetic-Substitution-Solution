from utils import calcFreq, read_dictionary
from random import randint
from polyglot.text import Text

class Guess:
    def __init__(self, ciphertext:str):
        self.ciph_text = ciphertext.replace(" ", "")
        self.guess = ""
        self.ciph = ciphertext
        self.ct_to_pt = {}
        self.reset()

    def reset(self):
        """Initializes the guess based on frequencies, modifies ct_to_pt as necessary"""
        freq_list = "etaoinshrdlcumwfgypbvkjxqz"
        desc_order = calcFreq(self.ciph_text)
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
        word_list = self.num_words(get_words=True)
        ct = self.ciph
        for word in word_list:
            ct.replace(word, "")
        if len(ct) == 0:
            return True
        return False
 
    def num_words(self, test=False, get_words=False):
        """Counts the number of words decrypted in the ciphertext"""
        if test:
            blob = self.ciph_text
        else:
            blob = self.guess
        text = Text(blob)
        text.language = "en"
        words = text.morphemes
        word_list = []
        dictionary = read_dictionary()
        for word in words:
            if word in dictionary:
                if len(word) >= 1 or word == 'a' or word == 'i':
                    word_list.append(word)
        if get_words:
            return word_list
        return len(word_list)
    
    def random_swap_neigh_chars(self):
       ct_list = self.ct_to_pt.keys()
       x = randint(0, len(ct_list)-2)
       self.swap_general(x)
       return x

    def swap_general(self, x, test=False):
        """Swaps two neighboring letters"""
        ct_list = list(self.ct_to_pt.keys())
        pt_list = list(self.ct_to_pt.values())
        char = pt_list[x]
        try:
            pt_list[x] = pt_list[x+1]
        except IndexError:
            print(x)
            return
        pt_list[x+1] = char
        for i in range(len(ct_list)):
            self.ct_to_pt[ct_list[i]] = pt_list[i]
        self.decode_ct()

    #Bug in the code!!!
    def decode_ct(self):
        """Encodes the ciphertext with the proposed plaintext given the key"""
        c = self.ciph
        for i in range(len(c)):
            c = c[0:i] + self.ct_to_pt[c[i]] + c[i+1:len(c)]
        self.guess = c

if __name__ == "__main__":
    g = Guess("mymotherwasverybeautifulonce")
    g.random_swap_neigh_chars()
    #testing git using command line