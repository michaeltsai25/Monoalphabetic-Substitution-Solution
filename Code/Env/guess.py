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
    
    """
    #Spurious key occurs, possibly rewrite this method
    def num_words(self, test=False):
        Counts the number of words decrypted in the guess
        if test == True:
            g = self.ciph_text
        else:
            g = self.guess
        count = 0
        with open('com_word_dic.txt', 'r') as new_file:
            file = new_file.read()
            word_list = file.split("\n")
            for word in word_list:
                if word in g: #self.guess:
                    print(g)
                    print(word)
                    g = g.replace(word, "")
                    count += 1
        return count, g

    """

    def num_words(self, test=False): #works if words are all at the front of the text, need to edit
        """Counts the number of words decrypted so far in the guess"""
        dic = self.__read_dictionary()
        num = 0
        if test:
            text = self.ciph_text
        else:
            text = self.guess
        x = 0
        i = 0
        while i < len(text):
            try:
                index = dic.index(text[x:i])
                i = self.__part_of_larger_word(text, x, i)
                x = i
                num += 1
                continue
            except:
                i += 1
        try:
            dic.index(text[x:i])
            num += 1
        except:
            pass
        return num

    def __part_of_larger_word(self, text, x, i):
        rel_words = self.__get_rel_words(text[x:i])
        j = i
        str_rel = ""
        for word in rel_words:
            str_rel += word
            str_rel += " "
        while text[x:j] in str_rel and j != len(text):
            j += 1
        j = j-1
        if rel_words.index(text[x:j]) != -1:
            return j
        else:
            return i
        
    def __get_rel_words(self, word):
        dic = self.__read_dictionary()
        lower = dic.index(word)
        upper = dic.index(word)
        while word in dic[upper]:
            upper += 1
        rel_words = dic[lower:upper]
        return rel_words

    def __read_dictionary(self):
        with open("/Users/michaeltsai/Documents/GitHub/Monoalphabetic-Substitution-Solution/com_word_dic.txt", 'r') as new_file:
            dic = new_file.read()
            dic = dic.split('\n')
        return dic
    
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
    g = Guess("testonefjfjfjfjtesttwo")
    print(g.num_words(test=True))