import utils

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